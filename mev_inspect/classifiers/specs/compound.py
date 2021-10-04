from mev_inspect.schemas.classified_traces import (
    Classification,
    ClassifierSpec,
    Protocol,
)

COMPOUND_V2_CETH_SPEC = ClassifierSpec(
    abi_name="CEther",
    protocol=Protocol.compound_v2,
    classifications={
        "liquidateBorrow(address,address)": Classification.liquidate,
        "seize(address,address,uint256)": Classification.seize,
    },
)

COMPOUND_V2_CTOKEN_SPEC = ClassifierSpec(
    abi_name="CToken",
    protocol=Protocol.compound_v2,
    classifications={
        "liquidateBorrow(address,uint256,address)": Classification.liquidate,
        "seize(address,address,uint256)": Classification.seize,
    },
)


COMPOUND_CLASSIFIER_SPECS = [
    COMPOUND_V2_CETH_SPEC,
    COMPOUND_V2_CTOKEN_SPEC
]