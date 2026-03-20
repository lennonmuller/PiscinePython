from typing import Any, List, Dict, Union, Protocol
from abc import ABC, abstractmethod


class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id: str) -> None:
        self.stages: List[ProcessingPipeline] = []
        self.pipeline_id = pipeline_id

    def add_stage(self, stage: str) -> None:
        self.stages.append(stage)

    @abstractmethod
    def process(self, data: Any) -> Any:
        ...


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        ...


class InputStage(ProcessingStage):
    def process(self, data: Any) -> Dict:
        processed_data = {}

        if not data:
            return {}

        if isinstance(data, dict):
            valid_keys = {"sensor", "value", "unit"}
            valid_units = ["C", "F"]
            if set(data.keys()) != valid_keys:
                raise TypeError(f"Missing or extra keys. "
                                f"Expected {list(valid_keys)}")
            if isinstance(data["sensor"], str):
                processed_data.update({"sensor": data.get("sensor")})
            else:
                raise TypeError(f"Value {data['sensor']} invalid")
            if isinstance(data["value"], (int, float)):
                processed_data.update({"value": data.get("value")})
            else:
                raise TypeError(f"Value {data['value']} invalid")
            if not isinstance(data["unit"], str):
                raise TypeError(f"Value {data['unit']} invalid")
            if data["unit"] in valid_units:
                processed_data.update({"unit": data.get("unit")})
            else:
                raise TypeError(f'Invalid Unit: {data["unit"]}. '
                                f'Expected {valid_units}')

        elif isinstance(data, str):
            valid_data = {"user", "action", "timestamp"}
            if "," not in data:
                raise ValueError("Invalid input. "
                                 "Expected CSV (comma-separated)")
            data = [token.strip() for token in data.split(",")]
            if not valid_data.issubset(set(data)):
                raise ValueError(f"Missing input. "
                                 f"Expected all of {valid_data}")
            for d in data:
                if d not in valid_data:
                    raise ValueError(f"Input '{d}' invalid. "
                                     f"Expected {valid_data}")
                else:
                    if d not in processed_data.keys():
                        processed_data[d] = 1
                    else:
                        processed_data[d] += 1

        elif isinstance(data, list):
            count = 0
            for d in data:
                if isinstance(d, (int, float)):
                    count += 1
                    processed_data.update({f"R{count}": d})
                else:
                    raise TypeError(f"Invalid input format: '{d}'. "
                                    f"Expected a number")

        return processed_data


