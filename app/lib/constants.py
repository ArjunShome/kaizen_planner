import string

DEFAULT_ERROR_MESSAGE = 'An error has occurred while processing your request.'

# User Types
USER_TYPE_INDIVIDUALS = 'Individuals'
USER_TYPE_OTHERS = 'Others'
USER_TYPE_DEFAULT = 'Default'
USER_TYPE_ADMIN = 'Admin'

UUID_PATTERN = '[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}'

# kaizen question segment
KAIZEN = "kaizen"
KAIZEN_PERFROMANCE_PARMETER = "kaizen_performance_parameter"
KAIZEN_DEVELOPMENT_SOLUTION = "kaizen_development_solution"
KAIZEN_IMPLEMENTATION_PLAN = "kaizen_implementation_plan"
KAIZEN_KEY_OUTCOME = "kaizen_key_outcome"
KAIZEN_ANALYSIS = "kaizen_analysis"

# kaizen_type
PROACTIVE_KAIZEN = "proactive"
REACTIVE_KAIZEN = "reactive"
INNOVATIVE_KAIZEN = "innovative"

# kaizen_source
CLIENT = "client_requirement"
SELF = "self_implemented"

# kaizen_status
IN_PROGRESS = "in_progress"
COMPLETED = "completed"

# kaizen_parameter_type
PRIMARY = "primary"
SECONDARY = "secondary"

# kaizen_evaluation_status
SUCCESS = 'Success'
FAILURE = 'Failure'
CHANGE = 'Change'

# kaizen_analysis_type
HOW_HOW = 'how_how'
BRAINSTORMING = 'brainstorming'
VALUE_STRAM_MAPPING = 'value_stream_mapping'
FIVE_WHY_ANALYSIS = '5_why_analysis'
FOUR_M_METHOD = '4m_method'
CAUSE_EFFECT_ANALYSIS = 'cause_affect_analysis'

# kaizen_outcome_type
SUCCESS_ITEM = 'success_item'
FAILURE_ITEM = 'failure_item'
FUTURE_IMPROVEMENT = 'future_improvement'
PERSONAL_BENEFIT = 'personal_benefit'
TEAM_BENEFIT = 'team_benefit'
ORGANIZATION_BENEFIT = 'organization_benefit'
CLIENT_BENEFIT = 'client_benefit'
TAKE_AWAYS = 'take_aways'

# kaizen_performance_metric
TIME = 'time'
COST = 'cost'
QUALITY = 'quality'

CC_EMAIL_LIST = ["arjun.shome@senecaglobal.com"]
