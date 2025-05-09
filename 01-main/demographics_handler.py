from datetime import datetime

class DemographicsHandler:
     """
    Handles demographic information to check if an MPIN is based on 
    sensitive personal dates like DOB, spouse DOB, or anniversary.
    """



    def __init__(self, dob: str, spouse_dob: str, anniversary: str):
        """
        Initializes the handler with user-specific demographic dates.
        
        Args:
            dob (str): Date of Birth in 'YYYY-MM-DD' format.
            spouse_dob (str): Spouse's Date of Birth in 'YYYY-MM-DD' format.
            anniversary (str): Wedding Anniversary in 'YYYY-MM-DD' format.
        """
        self.dob = dob
        self.spouse_dob = spouse_dob
        self.anniversary = anniversary



    def is_based_on_dob(self, mpin: str):
        """
        Checks if the MPIN contains any part of the user's own DOB.
        Returns: True if MPIN is based on year, month, or day from DOB.
        """

        dob_parts = [self.dob[:4], self.dob[5:7], self.dob[8:]]  # ['YYYY', 'MM', 'DD']
        return any(part in mpin for part in dob_parts)
    


    def is_based_on_spouse_dob(self, mpin: str):
        """
        Checks if the MPIN contains any part of the spouse's DOB.
        Returns:True if MPIN includes year, month, or day from spouse's DOB.
        """
        spouse_parts = [self.spouse_dob[:4], self.spouse_dob[5:7], self.spouse_dob[8:]]  # ['YYYY', 'MM', 'DD']
        return any(part in mpin for part in spouse_parts)
    


    def is_based_on_anniversary(self, mpin: str):
        """
        Checks if the MPIN includes parts of the wedding anniversary.

        Returns:
            bool: True if MPIN includes year, month, or day from anniversary.
        """
        anniversary_parts = [self.anniversary[:4], self.anniversary[5:7], self.anniversary[8:]]  # ['YYYY', 'MM', 'DD']
        return any(part in mpin for part in anniversary_parts)
