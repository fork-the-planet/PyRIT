# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

from pyrit.models import PromptDataType
from pyrit.prompt_converter import ConverterResult, PromptConverter


class SuffixAppendConverter(PromptConverter):
    """
    Appends a specified suffix to the prompt.
    E.g. with a suffix `!!!`, it converts a prompt of `test` to `test !!!`.

    See https://github.com/Azure/PyRIT/tree/main/pyrit/auxiliary_attacks/gcg for adversarial suffix generation.
    """

    def __init__(self, *, suffix: str):
        if not suffix:
            raise ValueError("Please specify a suffix (str) to be appended to the prompt.")

        self.suffix = suffix

    async def convert_async(self, *, prompt: str, input_type: PromptDataType = "text") -> ConverterResult:
        if not self.input_supported(input_type):
            raise ValueError("Input type not supported")

        return ConverterResult(output_text=prompt + " " + self.suffix, output_type="text")

    def input_supported(self, input_type: PromptDataType) -> bool:
        return input_type == "text"

    def output_supported(self, output_type: PromptDataType) -> bool:
        return output_type == "text"
