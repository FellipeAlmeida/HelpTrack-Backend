from typing import Annotated
from pydantic import StringConstraints, AfterValidator
import re

def validate_cnpj(value: str) -> str:

    value = value.strip().upper()

    cnpj = re.sub(r"[./-]", "", value)

    if len(cnpj) != 14:
        raise ValueError("CNPJ deve possuir 14 caracteres")

    if not cnpj.isalnum():
        raise ValueError("CNPJ possui caracteres inválidos")

    if not cnpj[-2:].isdigit():
        raise ValueError("Os dois últimos caracteres do CNPJ devem ser numéricos")

    return cnpj

CnpjStr = Annotated[
    str,
    AfterValidator(validate_cnpj)
]