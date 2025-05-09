import pytest
from main.mpin_validator import MPINValidator
from main.demographics_handler import DemographicsHandler

# Fixture that provides consistent sample user data to all tests
@pytest.fixture
def demographics():
    return DemographicsHandler(
        dob="1998-02-01",            # Self DOB
        spouse_dob="1998-03-05",     # Spouse DOB
        anniversary="2022-06-15"     # Wedding Anniversary
    )

# Parametrized test function for 20 MPIN scenarios
@pytest.mark.parametrize("mpin,expected_strength,expected_reasons", [

    # Very common PINs (known weak patterns)
    ("1234", "WEAK", ["COMMONLY_USED"]),
    ("1122", "WEAK", ["COMMONLY_USED"]),
    ("0000", "WEAK", ["COMMONLY_USED"]),
    ("9999", "WEAK", ["COMMONLY_USED"]),
    ("1212", "WEAK", ["COMMONLY_USED"]),
    ("1111", "WEAK", ["COMMONLY_USED"]),
    ("abcd", "WEAK", ["COMMONLY_USED"]),  # Alphanumeric assumed invalid/weak

    # Personal DOB-based weaknesses
    ("0201", "WEAK", ["DEMOGRAPHIC_DOB_SELF"]),     # DDMM of self DOB
    ("1998", "WEAK", ["DEMOGRAPHIC_DOB_SELF"]),     # YYYY of self DOB
    ("9802", "WEAK", ["DEMOGRAPHIC_DOB_SELF"]),     # YYMM of self DOB
    ("0102", "WEAK", ["DEMOGRAPHIC_DOB_SELF"]),     # Reversed DDMM

    # Spouse DOB-related weaknesses
    ("0503", "WEAK", ["DEMOGRAPHIC_DOB_SPOUSE"]),   # DDMM of spouse DOB
    ("0605", "WEAK", ["DEMOGRAPHIC_DOB_SPOUSE"]),   # Reversed MMDD

    # Anniversary-related weaknesses
    ("1506", "WEAK", ["DEMOGRAPHIC_ANNIVERSARY"]),  # DDMM of anniversary
    ("202206", "WEAK", ["DEMOGRAPHIC_ANNIVERSARY"]),# Full YYYYMM

    # Mixed personal data in PIN
    ("199815", "WEAK", ["DEMOGRAPHIC_DOB_SELF", "DEMOGRAPHIC_ANNIVERSARY"]),  # Combined values

    # Boundary testing
    ("1530", "STRONG", []),                         # Edge values, non-demographic
    ("5732", "STRONG", []),                         # Completely random
    ("927463", "STRONG", []),                       # Valid 6-digit PIN
    ("199802", "WEAK", ["DEMOGRAPHIC_DOB_SELF"]),   # Mixed year and month from DOB
])
def test_mpin_strength(demographics, mpin, expected_strength, expected_reasons):
    """
    Tests whether MPINs are classified correctly as WEAK or STRONG,
    and whether appropriate reasons are included in case of weakness.
    """
    # Instantiate validator with MPIN and demographics
    validator = MPINValidator(mpin, demographics)
    
    # Run the validation
    result = validator.validate_mpin()

    # Assert strength is as expected
    assert result["strength"] == expected_strength

    # Assert all expected reasons appear in the result
    for reason in expected_reasons:
        assert reason in result["reasons"]

    # Strong MPINs should not have any reasons
    if expected_strength == "STRONG":
        assert len(result["reasons"]) == 0
