from main.constants import COMMON_PIN_LIST
from main.demographics_handler import DemographicsHandler

class MPINValidator:
    def __init__(self, mpin: str, demographics: DemographicsHandler):
        self.mpin = mpin
        self.demographics = demographics

    def validate_mpin(self):
        reasons = []
        strength = 'STRONG'

        # Check for commonly used MPIN
        if self.mpin in COMMON_PIN_LIST:
            reasons.append("COMMONLY_USED")
            strength = 'WEAK'

        # Check if the MPIN is based on the user's demographics
        if self.demographics.is_based_on_dob(self.mpin):
            reasons.append("DEMOGRAPHIC_DOB_SELF")
            strength = 'WEAK'
        if self.demographics.is_based_on_spouse_dob(self.mpin):
            reasons.append("DEMOGRAPHIC_DOB_SPOUSE")
            strength = 'WEAK'
        if self.demographics.is_based_on_anniversary(self.mpin):
            reasons.append("DEMOGRAPHIC_ANNIVERSARY")
            strength = 'WEAK'

        return {
            'strength': strength,
            'reasons': reasons
        }
