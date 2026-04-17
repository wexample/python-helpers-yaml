from __future__ import annotations

from wexample_helpers.classes.mixin.has_env_keys_file import HasEnvKeysFile
from wexample_helpers.decorator.base_class import base_class


@base_class
class HasYamlEnvKeysFile(HasEnvKeysFile):
    """Mixin for classes that need to load env from files."""

    def _init_env_file_yaml(self, file_path: str) -> None:
        import os

        from wexample_helpers_yaml.helpers.yaml_helpers import yaml_read_dict

        loaded = yaml_read_dict(file_path)
        self.env_config.update(loaded)
        os.environ.update({k: v for k, v in loaded.items() if v is not None})
        self._validate_env_keys()
