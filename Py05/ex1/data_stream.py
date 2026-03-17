from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataStream(ABC):
    def ___init___(self, stream_id: str) -> None:
        self.stream_id = stream_id

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"Stream ID": self.stream_id}

    @abstractmethod
    def format_batch(self, data_batch: List[Any]) -> str:
        pass

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        return data_batch


class SensorStream(DataStream):
    def ___init___(self, stream_id: str) -> None:
        super().___init___(stream_id)
        self.type = "Environmental Data"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats.update({"Type": self.type})
        return stats

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        filtered_batch = []
        for data in data_batch:
            for key, value in data.items():
                if isinstance(key, (str)) and isinstance(value, (float, int)):
                    if not criteria:
                        if (key == "temp" or key == "humidity"
                                or key == "pressure"):
                            filtered_batch.append(data)
                    elif criteria == "High-priority":
                        if key == "pressure" and (value >= 1050 or value < 90):
                            filtered_batch.append(data)
                        elif key == "temp" and (value >= 27 or value < 8):
                            filtered_batch.append(data)
                        elif key == "humidity" and (value >= 75 or value < 20):
                            filtered_batch.append(data)
        return filtered_batch


if __name__ == "__main__":
    ids = ("SENSOR_001", "TRANS_001", "EVENT_001")

    sensor = SensorStream(ids[0])