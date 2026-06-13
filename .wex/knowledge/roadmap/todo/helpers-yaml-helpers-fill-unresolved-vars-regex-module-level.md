# Hoist compiled regex to module level in yaml_fill_unresolved_vars

**Source**: `packages/helpers-yaml/src/wexample_helpers_yaml/helpers/yaml_helpers.py:20`
**Agent**: agent:performance
**Bucket**: restructure
**Severity**: perf

## Symptom
`re.compile(r"\$\{([^}]+)\}")` is called on every invocation of `yaml_fill_unresolved_vars`, recompiling the pattern each time even though it is a constant.

## Suggested direction
Extract the compiled pattern to a module-level constant (e.g. `_UNRESOLVED_VAR_RE`) so the regex is compiled once at import time and reused on every call.
