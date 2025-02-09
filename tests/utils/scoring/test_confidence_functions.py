from diagnostipy.core.models.symptom_rule import SymptomRule
from diagnostipy.utils.scoring.confidence_functions import (
    entropy_based_confidence,
    rule_coverage_confidence,
    weighted_confidence,
)


def test_weighted_confidence_with_conditions(rules_with_conditions):
    input_data = {"symptom1": 2, "symptom2": 0.3, "symptom3": True}
    applicable_rules = [
        rule for rule in rules_with_conditions if rule.applies(input_data)
    ]

    confidence = weighted_confidence(applicable_rules, rules_with_conditions)
    assert 0.0 <= confidence <= 1.0

    input_data = {"symptom1": 0.5, "symptom2": 2, "symptom3": False}
    applicable_rules = [
        rule for rule in rules_with_conditions if rule.applies(input_data)
    ]
    assert weighted_confidence(applicable_rules, rules_with_conditions) == 0.0


def test_entropy_based_confidence_with_conditions(rules_with_conditions):
    input_data = {"symptom1": 2, "symptom2": 0.3, "symptom3": True}
    applicable_rules = [
        rule for rule in rules_with_conditions if rule.applies(input_data)
    ]

    confidence = entropy_based_confidence(applicable_rules, rules_with_conditions)
    assert 0.0 <= confidence <= 1.0

    input_data = {"symptom1": 0.5, "symptom2": 2, "symptom3": False}
    applicable_rules = [
        rule for rule in rules_with_conditions if rule.applies(input_data)
    ]
    assert entropy_based_confidence(applicable_rules, rules_with_conditions) == 0.0


def test_rule_coverage_confidence_with_conditions(rules_with_conditions):
    input_data = {"symptom1": 2, "symptom2": 0.3, "symptom3": True}
    applicable_rules = [
        rule for rule in rules_with_conditions if rule.applies(input_data)
    ]
    confidence = rule_coverage_confidence(applicable_rules, rules_with_conditions)
    assert 0.0 <= confidence <= 1.0

    input_data = {"symptom1": 0.5, "symptom2": 2, "symptom3": False}
    applicable_rules = [
        rule for rule in rules_with_conditions if rule.applies(input_data)
    ]
    confidence = rule_coverage_confidence(applicable_rules, rules_with_conditions)
    assert confidence == 0.0

    confidence = rule_coverage_confidence(applicable_rules, rules_with_conditions)
    assert confidence == 0.0
    confidence = rule_coverage_confidence(applicable_rules, rules_with_conditions)
    assert confidence == 0.0


def test_weighted_confidence_with_zero_weights(rules_with_zero_weight):
    input_data = {"symptom1": 2, "symptom2": 0.3, "symptom3": True}
    applicable_rules = [
        rule for rule in rules_with_zero_weight if rule.applies(input_data)
    ]

    assert entropy_based_confidence(applicable_rules, rules_with_zero_weight) == 0.0


def test_weighted_confidence_with_no_possible_weight(rules_with_zero_weight):
    input_data = {"symptom1": 1, "symptom2": 0.5}
    applicable_rules = [
        rule for rule in rules_with_zero_weight if rule.applies(input_data)
    ]

    assert weighted_confidence(applicable_rules, rules_with_zero_weight) == 0.0


def test_rule_coverage_confidence_with_no_possible_rules():
    all_rules: list[SymptomRule] = []
    applicable_rules: list[SymptomRule] = []

    assert rule_coverage_confidence(applicable_rules, all_rules) == 0.0
