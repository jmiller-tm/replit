# standard libs
import json
import logging
import os
from dataclasses import dataclass, field
from typing import Dict, Tuple, Union

# common
from common.python.file_utils import load_file_contents

log = logging.getLogger(__name__)
logging.basicConfig(
    level=os.environ.get("LOGLEVEL", "INFO"),
    format="%(asctime)s.%(msecs)03d - %(levelname)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


@dataclass
class ServiceAccount:
    account_id: str = ""
    name: str = ""
    token: str = ""


@dataclass
class Environment:
    name: str
    basic_auth_username: str = ""
    basic_auth_password: str = ""
    core_api_url: str = ""
    ops_dash_url: str = ""
    data_loader_api_url: str = ""
    payments_hub_url: str = ""
    products_api_url: str = ""
    workflow_api_url: str = ""
    xpl_api_url: str = ""
    kafka_config: Dict[str, Union[bool, int, str]] = field(default_factory=dict)
    service_account: ServiceAccount = field(default_factory=ServiceAccount)
    performance_testing: bool = False
    prometheus_api_url: str = ""
    cluster: str = ""
    namespace: str = ""


def load_environment(name: str, env_definition: Dict) -> Environment:

    kafka_config = env_definition.pop("kafka", {})
    service_account_id = env_definition.pop("service_account_id")
    service_account_name = env_definition.pop("service_account_name")
    service_account_token = env_definition.pop("access_token")

    return Environment(
        name=name,
        kafka_config=kafka_config,
        service_account=ServiceAccount(
            account_id=service_account_id,
            name=service_account_name,
            token=service_account_token,
        ),
        **env_definition,
    )


def load_environments(file_path: str) -> Tuple[Environment, Dict[str, Environment]]:
    """
    Load a single environment from a JSON file
    :param file_path: path to the JSON file
    :return: default environment and environments, initialised from JSON file contents
    """

    all_envs = json.loads(load_file_contents(file_path))

    if "default_environment" not in all_envs:
        raise Exception(f"Key default_environment not found in config at {file_path}")

    default_environment_name = all_envs["default_environment"]
    if default_environment_name not in all_envs["environments"]:
        raise Exception(
            f"Default environment {default_environment_name} not found in config at {file_path}"
        )

    environments = {
        env_name: load_environment(env_name, env_definition=env)
        for env_name, env in all_envs["environments"].items()
    }

    return environments[default_environment_name], environments
