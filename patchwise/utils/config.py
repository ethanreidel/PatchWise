# Copyright (c) Qualcomm Technologies, Inc. and/or its subsidiaries.
# SPDX-License-Identifier: BSD-3-Clause

from patchwise import CONFIG_DIR, PACKAGE_PATH
import yaml

user_config_path = CONFIG_DIR / "patchwise_config.yaml"
default_config_path = PACKAGE_PATH / "default_config.yaml"


def read_from_user_config() -> dict:
    if user_config_path.exists():
        with open(user_config_path, "r") as file:
            config_dict = yaml.safe_load(file)
    else:
        raise FileNotFoundError(f"Path {user_config_path} does not exist.")
    return config_dict


def read_from_default_config() -> dict:
    with open(default_config_path, "r") as file:
        default_config_dict = yaml.safe_load(file)
    return default_config_dict


def parse_config():
    default_options = read_from_default_config()
    user_options = read_from_user_config()

    combined_options = {
        **default_options,
        **{k: v for k, v in user_options.items() if v is not None},
    }

    return combined_options
