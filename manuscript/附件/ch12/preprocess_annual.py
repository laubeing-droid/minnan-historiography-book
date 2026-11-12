#!/usr/bin/env python3
"""Chapter 12 teaching preprocessing, release status NOT_RUN.

Only Python standard-library modules are used. This program does not fit any
statistical model, compute ACF/PACF/ADF/KPSS/STL, score forecasts, fetch data,
install packages, delete files, or overwrite an existing output directory.
Input: one annual, comparable, non-negative count series selected from a CSV.
Output: one new directory separating origin-safe inputs from future truth.
The bundled CSV is synthetic and is not a recovered historical data set.
"""

import argparse
import csv
import hashlib
import json
import math
import platform
from datetime import datetime, timezone
from pathlib import Path


RELEASE_STATUS = "NOT_RUN"
REQUIRED = {
    "row_id", "series_id", "period", "y", "status", "unit", "measure",
    "boundary_version", "source_id", "availability_year", "date_precision",
    "data_kind", "note",
}
OBSERVED = {"observed", "observed_zero"}
MISSING = {"no_record", "illegible", "source_missing", "not_applicable"}
TRAIN_FIELDS = [
    "series_id", "period", "y", "input_y", "z", "observed_mask",
    "available_mask", "imputed_mask", "eligible_target", "status", "unit",
    "measure", "boundary_version", "source_id", "availability_year",
    "year_index", "years_since_last_observed", "origin", "data_kind",
]
TRUTH_FIELDS = [
    "series_id", "period", "y", "observed_mask", "eligible_target",
    "status", "unit", "measure", "boundary_version", "source_id",
    "availability_year", "data_kind", "use_restriction",
]


def integer_year(value, field):
    """Require a four-digit positive year, not a fabricated timestamp."""
    value = str(value).strip()
    if len(value) != 4 or not value.isascii() or not value.isdigit():
        raise ValueError(f"{field} must be a four-digit year: {value!r}")
    year = int(value)
    if not 1000 <= year <= 9999:
        raise ValueError(f"Unsupported year in {field}: {value!r}")
    return year


def read_selected(path, series_id):
    selected = {}
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if not REQUIRED.issubset(reader.fieldnames or []):
            missing = sorted(REQUIRED.difference(reader.fieldnames or []))
            raise ValueError(f"Missing columns: {missing}")
        for line_number, raw in enumerate(reader, start=2):
            if None in raw or any(v is None for v in raw.values()):
                raise ValueError(f"CSV field count mismatch at line {line_number}")
            row = {key: value.strip() for key, value in raw.items()}
            if row["series_id"] != series_id:
                continue
            period = integer_year(row["period"], "period")
            if period in selected:
                raise ValueError(f"Duplicate series/year key: {series_id}/{period}")
            if row["date_precision"] != "year":
                raise ValueError(f"Year precision required at line {line_number}")
            if row["status"] not in OBSERVED | MISSING:
                raise ValueError(f"Unknown status at line {line_number}")
            for field in ("row_id", "unit", "measure", "boundary_version",
                          "source_id", "data_kind"):
                if not row[field]:
                    raise ValueError(f"Empty {field} at line {line_number}")
            if row["status"] in OBSERVED:
                try:
                    value = float(row["y"])
                except ValueError as error:
                    raise ValueError(f"Observed value absent at {period}") from error
                if not math.isfinite(value) or value < 0 or not value.is_integer():
                    raise ValueError(f"Expected a finite non-negative count at {period}")
                if (value == 0) != (row["status"] == "observed_zero"):
                    raise ValueError(f"Zero and observed_zero must agree at {period}")
                available = integer_year(row["availability_year"], "availability_year")
                if available < period:
                    raise ValueError(f"Annual count available before its year at {period}")
            else:
                if row["y"] or row["availability_year"]:
                    raise ValueError(f"Missing value must remain blank at {period}")
                value, available = None, None
            row.update(period=period, y=value, availability_year=available)
            selected[period] = row
    if not selected:
        raise ValueError(f"No records for series {series_id!r}")
    # This teaching program deliberately rejects mixed measurement definitions.
    for field in ("unit", "measure", "boundary_version", "data_kind"):
        if len({row[field] for row in selected.values()}) != 1:
            raise ValueError(f"Mixed {field}; reconcile or split the series explicitly")
    return selected


def row_at(records, period, series_id):
    if period in records:
        return records[period]
    exemplar = records[min(records)]
    return {
        "row_id": "", "series_id": series_id, "period": period, "y": None,
        "status": "no_record", "unit": exemplar["unit"],
        "measure": exemplar["measure"],
        "boundary_version": exemplar["boundary_version"],
        "source_id": "", "availability_year": None, "date_precision": "year",
        "data_kind": exemplar["data_kind"], "note": "Inserted time position only",
    }


def prepare_train(records, args):
    rows, last_observed = [], None
    for period in range(args.train_start, args.origin + 1):
        raw = row_at(records, period, args.series_id)
        available = (raw["y"] is not None
                     and raw["availability_year"] <= args.origin)
        # All model-facing masks are origin-safe. A later-known observation is
        # not exposed as observed at an earlier origin. Raw archival status is
        # still present in the source CSV, but must not be used as a feature.
        value = raw["y"] if available else None
        status = raw["status"]
        if raw["y"] is not None and not available:
            status = "not_available"
        input_value, imputed = value, 0
        if available:
            last_observed = (period, value)
        elif (args.impute == "ffill1" and status == "no_record"
              and last_observed is not None
              and last_observed[0] == period - 1):
            input_value, imputed = last_observed[1], 1
        gap = None if last_observed is None else period - last_observed[0]
        rows.append({
            "series_id": args.series_id, "period": period, "y": value,
            "input_y": input_value, "z": None,
            "observed_mask": int(available), "available_mask": int(available),
            "imputed_mask": imputed, "eligible_target": int(available),
            "status": status, "unit": raw["unit"], "measure": raw["measure"],
            "boundary_version": raw["boundary_version"],
            "source_id": raw["source_id"],
            "availability_year": raw["availability_year"] if available else None,
            "year_index": period - args.train_start,
            "years_since_last_observed": gap, "origin": args.origin,
            "data_kind": raw["data_kind"],
        })
    values = [row["y"] for row in rows if row["observed_mask"] == 1]
    if not values:
        raise ValueError("No original observations available in this training interval")
    # Fitting is only a descriptive scale calculation; no statistical model.
    mean = math.fsum(values) / len(values)
    variance = math.fsum((value - mean) ** 2 for value in values) / len(values)
    empirical_scale = math.sqrt(variance)
    constant_train = empirical_scale == 0
    scale = 1.0 if constant_train else empirical_scale
    if args.scale == "standard":
        for row in rows:
            if row["input_y"] is not None:
                row["z"] = (row["input_y"] - mean) / scale
    parameters = {
        "method": args.scale,
        "series_id": args.series_id,
        "train_start": args.train_start,
        "origin": args.origin,
        "n_original_available": len(values),
        "mean": mean,
        "scale": scale,
        "variance_denominator": "n",
        "constant_train": constant_train,
        "imputation": args.impute,
        "fit_includes_imputed_values": False,
        "fit_includes_future_values": False,
        "inverse_transform": "y = mean + scale * z" if args.scale == "standard" else "identity",
        "seasonality": "none_assumed",
    }
    return rows, parameters


def prepare_truth(records, args):
    """An evaluator-only table: never return this to fit/transform functions."""
    rows = []
    for period in range(args.origin + 1, args.evaluation_end + 1):
        raw = row_at(records, period, args.series_id)
        observed = raw["y"] is not None
        rows.append({
            "series_id": args.series_id, "period": period, "y": raw["y"],
            "observed_mask": int(observed), "eligible_target": int(observed),
            "status": raw["status"], "unit": raw["unit"], "measure": raw["measure"],
            "boundary_version": raw["boundary_version"], "source_id": raw["source_id"],
            "availability_year": raw["availability_year"], "data_kind": raw["data_kind"],
            "use_restriction": "EVALUATION_ONLY_AFTER_LABEL_AVAILABLE",
        })
    return rows


def write_csv_new(path, fieldnames, rows):
    with path.open("x", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="raise")
        writer.writeheader()
        writer.writerows(rows)  # csv writes None as an empty field, never zero.


def write_json_new(path, value):
    with path.open("x", encoding="utf-8") as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2, allow_nan=False)
        handle.write("\n")


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True,
                        help="A new directory; existing paths are refused")
    parser.add_argument("--series-id", default="DEMO_PORT_A")
    parser.add_argument("--origin", type=int, required=True)
    parser.add_argument("--train-start", type=int, default=1900)
    parser.add_argument("--evaluation-end", type=int, default=1923)
    parser.add_argument("--impute", choices=("none", "ffill1"), default="none")
    parser.add_argument("--scale", choices=("none", "standard"), default="none")
    return parser.parse_args()


def main():
    args = parse_args()
    for name in ("train_start", "origin", "evaluation_end"):
        integer_year(getattr(args, name), name)
    if not args.train_start <= args.origin < args.evaluation_end:
        raise ValueError("Require train_start <= origin < evaluation_end")
    if not args.input.is_file():
        raise ValueError("Input CSV does not exist")
    if args.output.exists():
        raise FileExistsError("Output already exists; choose a new directory, do not overwrite")
    if not args.output.parent.is_dir():
        raise ValueError("Output parent directory must already exist")
    records = read_selected(args.input, args.series_id)
    if args.train_start < min(records) or args.evaluation_end > max(records):
        raise ValueError("Requested range exceeds source coverage; revise the task explicitly")
    train, parameters = prepare_train(records, args)
    truth = prepare_truth(records, args)
    # Refusal above happens before any output creation. If writing later fails,
    # retain the partial directory for inspection; never delete it automatically.
    args.output.mkdir(exist_ok=False)
    write_csv_new(args.output / "train_input.csv", TRAIN_FIELDS, train)
    write_csv_new(args.output / "evaluation_truth.csv", TRUTH_FIELDS, truth)
    write_json_new(args.output / "transform_params.json", parameters)
    write_json_new(args.output / "run_manifest.json", {
        "status": "PREPROCESSING_COMPLETED_BY_THIS_INVOCATION",
        "statistical_diagnostics": "NOT_RUN",
        "models": "NOT_RUN",
        "evaluation": "NOT_RUN",
        "source_release_status": RELEASE_STATUS,
        "executed_at_utc": datetime.now(timezone.utc).isoformat(),
        "python_version": platform.python_version(),
        "input_path": str(args.input.resolve()),
        "input_sha256": hashlib.sha256(args.input.read_bytes()).hexdigest(),
        "program_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "arguments": {key: str(value) if isinstance(value, Path) else value
                      for key, value in vars(args).items()},
        "train_rows": len(train), "evaluation_rows": len(truth),
        "data_kind": next(iter(records.values()))["data_kind"],
        "warning": "This is preprocessing only; no forecast or statistical result is established.",
    })
    print(f"Wrote a new preprocessing directory: {args.output}")


if __name__ == "__main__":
    main()
