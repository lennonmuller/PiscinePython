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

    def format_batch(self, data_batch: List[Any]) -> str:
        sensor_batch = []
        for data in data_batch:
            for key, value in data.items():
                list_item = f"{key}:{value}"
                sensor_batch.append(list_item)
        format_sensor_batch = (", ").join(sensor_batch)
        return f"{format_sensor_batch}"

    def process_batch(self, data_batch: List[Any]) -> str:
        count = 0
        temps = 0
        for data in data_batch:
            if "temp" in data:
                temps += float(data.get("temp", 0))
                count += 1
        temp_avg = temps / count
        return f"Sensor analysis: {len(data_batch)} readings processed, \
            avg temp: {temp_avg}°C"


class TransactionStream(DataStream):
    def ___init___(self, stream_id: str) -> None:
        super().___init___(stream_id)
        self.type = "Financial Data"

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
                        if key == "buy" or key == "sell":
                            filtered_batch.append(data)
                    elif criteria == "High-priority":
                        if (key == "buy" or key == "sell") and value >= 200:
                            filtered_batch.append(data)
        return filtered_batch

    def format_batch(self, data_batch: List[Any]) -> str:
        transaction_batch = []
        for data in data_batch:
            for key, value in data.items():
                list_item = f"{key}:{value}"
                transaction_batch.append(list_item)
        format_transaction_batch = (", ").join(transaction_batch)
        return f"{format_transaction_batch}"

    def process_batch(self, data_batch: List[Any]):
        buy = 0
        sell = 0
        for data in data_batch:
            buy += int(data.get("buy", 0))
            sell += int(data.get("sell", 0))
        if (buy - sell) > 0:
            net_flow = f"+{buy - sell}"
        return f"Transaction analysis: {len(data_batch)} operations, \
            net flow: {net_flow} units"


if __name__ == "__main__":
    ids = ("SENSOR_001", "TRANS_001", "EVENT_001")

    sensor = SensorStream(ids[0])
    trans = TransactionStream(ids[1])

    s_batch = [{'temp': 22.5}, {'humidity': 65}, {'pressure': 1013}]
    t_batch = [{'buy': 100}, {'sell': 150}, {'buy': 75}]

    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    print("\nInitializing Sensor Stream...")
    print(", ".join([f"{k}: {v}" for k, v in sensor.get_stats().items()]))
    sf_batch = sensor.filter_data(s_batch)
    if sf_batch:
        print(f"Processing sensor batch: [{sensor.format_batch(sf_batch)}]")
        print(f"{sensor.process_batch(sf_batch)}")
    else:
        print("ERROR: Sensor values invalid.")

    print("\nInitializing Transaction Stream...")
    print(", ".join([f"{k}: {v}" for k, v in trans.get_stats().items()]))
    tfbatch = trans.filter_data(t_batch)
    if tfbatch:
        print(f"Processing transaction batch: [{trans.format_batch(tfbatch)}]")
        print(f"{trans.process_batch(tfbatch)}")
    else:
        print("ERROR: Transaction values invalid.")
