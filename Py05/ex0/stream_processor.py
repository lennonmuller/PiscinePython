from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if data is None:
            return False
        try:
            return all([isinstance(num, (int, float)) for num in data])
        except TypeError:
            return False

    def process(self, data: Any) -> str:
        num = len(data)
        n_sum = sum(d for d in data)
        n_avg = n_sum / num
        return f"Processed {num} numeric values, sum={n_sum}, avg={n_avg:.1f}"

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and bool(data)

    def process(self, data: Any) -> str:
        chars = len(data)
        word_count = len(data.split())
        return f"Processed text: {chars} characters, {word_count} words"

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if data is None:
            return False
        if isinstance(data, str) and bool(data) and ("ERROR" in data or "INFO"
                                                     in data):
            return True
        return False

    def process(self, data: Any) -> str:
        if "ERROR" in data:
            log_type = "ALERT"
            log_level = "ERROR"
        elif "INFO" in data:
            log_type = "INFO"
            log_level = log_type
        before, sep, after = data.partition(':')
        return f"[{log_type}] {log_level} level detected:{after}"

    def format_output(self, result: str) -> str:
        return super().format_output(result)


if __name__ == "__main__":
    num_data = [1, 2, 3, 4, 5]
    str_data = "Hello Nexus World"
    logstr_data = "ERROR: Connection timeout"

    numeric_data = NumericProcessor()
    text_data = TextProcessor()
    log_data = LogProcessor()

    process_data = ([1, 2, 3], "Hello World!", "INFO: System ready")
    processors = (numeric_data, text_data, log_data)

    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    print("\nInitializing Numeric Processor...")
    print(f"Processing data: {num_data}")
    if numeric_data.validate(num_data):
        print("Validation: Numeric data verified")
        numeric_result = numeric_data.process(num_data)
        print(f"{numeric_data.format_output(numeric_result)}")
    else:
        print("Validation ERROR: data non-numeric")

    print("\nInitializing Text Processor...")
    print(f'Processing data: "{str_data}"')
    if text_data.validate(str_data):
        print("Validation: Text data verified")
        text_result = text_data.process(str_data)
        print(f"{text_data.format_output(text_result)}")
    else:
        print("Validation ERROR: data non-textual")

    print("\nInitializing Log Processor...")
    print(f'Processing data: "{logstr_data}"')
    if log_data.validate(logstr_data):
        print("Validation: Log entry verified")
        log_result = log_data.process(logstr_data)
        print(f"{log_data.format_output(log_result)}")
    else:
        print("Validation ERROR: log entry not found")

    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through the same interface...")
    i = 0
    for pd in process_data:
        print(f"Result {i + 1}: {processors[i].process(pd)}")
        i += 1

    print("\nFoundation systems online. Nexus ready for advanced streams.")
