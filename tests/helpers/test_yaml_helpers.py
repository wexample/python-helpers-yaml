from __future__ import annotations

from pathlib import Path


def test_yaml_fill_unresolved_vars_replaces_multiple() -> None:
    from wexample_helpers_yaml.helpers.yaml_helpers import yaml_fill_unresolved_vars

    assert yaml_fill_unresolved_vars("${A}-${B}", fill_value="z") == "z-z"


def test_yaml_fill_unresolved_vars_replaces_with_empty_by_default() -> None:
    from wexample_helpers_yaml.helpers.yaml_helpers import yaml_fill_unresolved_vars

    assert yaml_fill_unresolved_vars("a: ${FOO}") == "a: "


def test_yaml_fill_unresolved_vars_uses_fill_value() -> None:
    from wexample_helpers_yaml.helpers.yaml_helpers import yaml_fill_unresolved_vars

    assert yaml_fill_unresolved_vars("a: ${FOO}", fill_value="X") == "a: X"


def test_yaml_read_dict_returns_default_when_empty(tmp_path: Path) -> None:
    from wexample_helpers_yaml.helpers.yaml_helpers import yaml_read_dict

    assert yaml_read_dict(tmp_path / "missing.yml", default={"x": 1}) == {"x": 1}


def test_yaml_read_dict_returns_empty_dict_when_missing(tmp_path: Path) -> None:
    from wexample_helpers_yaml.helpers.yaml_helpers import yaml_read_dict

    assert yaml_read_dict(tmp_path / "missing.yml") == {}


def test_yaml_read_returns_default_on_missing_file(tmp_path: Path) -> None:
    from wexample_helpers_yaml.helpers.yaml_helpers import yaml_read

    assert yaml_read(tmp_path / "missing.yml", default={"d": 1}) == {"d": 1}


def test_yaml_read_returns_default_on_non_dict(tmp_path: Path) -> None:
    from wexample_helpers_yaml.helpers.yaml_helpers import yaml_read

    file_path = tmp_path / "scalar.yml"
    file_path.write_text("- just\n- a\n- list\n")
    assert yaml_read(file_path, default="fallback") == "fallback"


def test_yaml_read_returns_dict(tmp_path: Path) -> None:
    from wexample_helpers_yaml.helpers.yaml_helpers import yaml_read

    file_path = tmp_path / "data.yml"
    file_path.write_text("key: value\nnum: 3\n")
    assert yaml_read(file_path) == {"key": "value", "num": 3}


def test_yaml_write_then_read_roundtrip(tmp_path: Path) -> None:
    from wexample_helpers_yaml.helpers.yaml_helpers import yaml_read, yaml_write

    file_path = tmp_path / "out.yml"
    yaml_write(file_path, {"a": 1, "b": "two"})
    assert yaml_read(file_path) == {"a": 1, "b": "two"}
