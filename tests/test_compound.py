from typing import List

from mev_inspect.compound_liquidations import get_compound_liquidations, get_all_comp_markets
from mev_inspect.schemas.liquidations import Liquidation
from mev_inspect.schemas.classified_traces import Protocol
from mev_inspect.classifiers.trace import TraceClassifier
from tests.utils import load_test_block
from web3 import Web3
import os

rpc = os.getenv("RPC_URL")

if rpc is None:
    raise RuntimeError("Missing environment variable RPC_URL")
else:
    w3 = Web3(Web3.HTTPProvider(rpc))


def test_c_ether_liquidations():
    block_number = 13234998
    transaction_hash = "0x78f7e67391c2bacde45e5057241f8b9e21a59330bce4332eecfff8fac279d090"

    liquidations = [
        Liquidation(
            liquidated_user="0xb5535a3681cf8d5431b8acfd779e2f79677ecce9",
            liquidator_user="0xe0090ec6895c087a393f0e45f1f85098a6c33bef",
            collateral_token_address="0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
            debt_token_address="0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
            debt_purchase_amount=268066492249420078,
            received_amount=105283041640,
            protocol=Protocol.compound_v2,
            transaction_hash=transaction_hash,
            trace_address=[1],
            block_number=block_number,
        )
    ]
    block = load_test_block(block_number)
    trace_classifier = TraceClassifier()
    classified_traces = trace_classifier.classify(block.traces)
    comp_markets = get_all_comp_markets(w3)
    result = get_compound_liquidations(classified_traces, comp_markets, w3)
    assert result == liquidations

    block_number = 13326607
    transaction_hash = "0x42a575e3f41d24f3bb00ae96f220a8bd1e24e6a6282c2e0059bb7820c61e91b1"

    liquidations = [
        Liquidation(
            liquidated_user="0x45df6f00166c3fb77dc16b9e47ff57bc6694e898",
            liquidator_user="0xe0090ec6895c087a393f0e45f1f85098a6c33bef",
            collateral_token_address="0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
            debt_token_address="0x1f9840a85d5af5bf1d1762f925bdaddc4201f984",
            debt_purchase_amount=414547860568297082,
            received_amount=6512886969,
            protocol=Protocol.compound_v2,
            transaction_hash=transaction_hash,
            trace_address=[1],
            block_number=block_number,
        )
    ]
    block = load_test_block(block_number)
    trace_classifier = TraceClassifier()
    classified_traces = trace_classifier.classify(block.traces)
    comp_markets = get_all_comp_markets(w3)
    result = get_compound_liquidations(classified_traces, comp_markets, w3)
    assert result == liquidations

    block_number = 13326607
    transaction_hash = "0x22a98b27a1d2c4f3cba9d65257d18ee961d6c98f21c7eade37da0543847eb654"

    liquidations = [
        Liquidation(
            liquidated_user="0xacbcf5d2970eef25f02a27e9d9cd31027b058b9b",
            liquidator_user="0xe0090ec6895c087a393f0e45f1f85098a6c33bef",
            collateral_token_address="0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
            debt_token_address="0x1f9840a85d5af5bf1d1762f925bdaddc4201f984",
            debt_purchase_amount=1106497772527562662,
            received_amount=18427226261,
            protocol=Protocol.compound_v2,
            transaction_hash=transaction_hash,
            trace_address=[1],
            block_number=block_number,
        )
    ]
    block = load_test_block(block_number)
    trace_classifier = TraceClassifier()
    classified_traces = trace_classifier.classify(block.traces)
    comp_markets = get_all_comp_markets(w3)
    result = get_compound_liquidations(classified_traces, comp_markets, w3)
    assert result == liquidations

def test_c_token_liquidation():
    block_number = 13326607
    transaction_hash = "0x012215bedd00147c58e1f59807664914b2abbfc13c260190dc9cfc490be3e343"

    liquidations = [
        Liquidation(
            liquidated_user="0xacdd5528c1c92b57045041b5278efa06cdade4d8",
            liquidator_user="0xe0090ec6895c087a393f0e45f1f85098a6c33bef",
            collateral_token_address="0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
            debt_token_address="0xc00e94cb662c3520282e6f5717214004a7f26888",
            debt_purchase_amount=1207055531,
            received_amount=436574331,
            protocol=Protocol.compound_v2,
            transaction_hash=transaction_hash,
            trace_address=[1],
            block_number=block_number,
        )
    ]
    block = load_test_block(block_number)
    trace_classifier = TraceClassifier()
    classified_traces = trace_classifier.classify(block.traces)
    comp_markets = get_all_comp_markets(w3)
    result = get_compound_liquidations(classified_traces, comp_markets, w3)
    assert result == liquidations

