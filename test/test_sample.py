from src.sample import add
import pytest

# テスト（成功パターン）


def test_expected():
    assert add(3, 5) == 8

# テスト（失敗パターン）


def test_unexpected():
    assert add(3, 5) == 10
