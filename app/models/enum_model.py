from enum import Enum

from app.lib import constants


class KaizenQuestionSegment(str, Enum):
    KAIZEN = constants.KAIZEN
    KAIZEN_PERFORMANCE_PARAMETER = constants.KAIZEN_PERFROMANCE_PARMETER
    KAIZEN_DEVELOPMENT_SOLUTION = constants.KAIZEN_DEVELOPMENT_SOLUTION
    KAIZEN_IMPLEMENTATION_PLAN = constants.KAIZEN_IMPLEMENTATION_PLAN
    KAIZEN_KEY_OUTCOME = constants.KAIZEN_KEY_OUTCOME
    KAIZEN_ANALYSIS = constants.KAIZEN_ANALYSIS


class KaizenType(str, Enum):
    PROACTIVE = constants.PROACTIVE_KAIZEN
    REACTIVE = constants.REACTIVE_KAIZEN
    INNOVATIVE = constants.INNOVATIVE_KAIZEN


class KaizenSource(str, Enum):
    CLIENT_REQUIREMENT = constants.CLIENT
    SELF_IMPLEMENTED = constants.SELF


class KaizenStatus(str, Enum):
    IN_PROGRESS = constants.IN_PROGRESS
    COMPLETED = constants.COMPLETED


class KaizenParameterType(str, Enum):
    PRIMARY = constants.PRIMARY
    SECONDARY = constants.SECONDARY


class KaizenAnalysisType(str, Enum):
    HOW_HOW = constants.HOW_HOW
    BRAINSTORMING = constants.BRAINSTORMING
    VALUE_STREAM_MAPPING = constants.VALUE_STRAM_MAPPING
    FIVE_WHY_ANALYSIS = constants.FIVE_WHY_ANALYSIS
    FOUR_M_METHOD = constants.FOUR_M_METHOD
    CAUSE_AFFECT_ANALYSIS = constants.CAUSE_EFFECT_ANALYSIS


class KaizenOutcomeType(str, Enum):
    SUCCESS_ITEM = constants.SUCCESS_ITEM
    FAILURE_ITEM = constants.FAILURE_ITEM
    FUTURE_IMPROVEMENT = constants.FUTURE_IMPROVEMENT
    PERSONAL_BENEFIT = constants.PERSONAL_BENEFIT
    TEAM_BENEFIT = constants.TEAM_BENEFIT
    ORGANIZATION_BENEFIT = constants.ORGANIZATION_BENEFIT
    CLIENT_BENEFIT = constants.CLIENT_BENEFIT
    TAKE_AWAYS = constants.TAKE_AWAYS


class KaizenPerformanceMetric(str, Enum):
    TIME = constants.TIME
    COST = constants.COST
    QUALITY = constants.QUALITY
