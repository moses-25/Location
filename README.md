# Phone Number Tools

This workspace contains two Python scripts designed to analyze phone numbers and provide information such as location, timezone, carrier, and county mapping (specific to Kenya). The scripts use libraries like `phonenumbers` and `colorama` for functionality and enhanced user experience.

---

## Files in the Workspace

### 1. `Location.py`
A tool for extracting detailed information about a phone number.

#### Features:
- Validates phone numbers.
- Provides the following details:
  - **Timezone**: The time zone(s) associated with the phone number.
  - **Location**: The geographical location of the phone number.
  - **Carrier**: The service provider for the phone number.
- Displays information in a user-friendly format with colored output.

#### Usage:
Run the script and input a phone number with the country code (e.g., `+2547XXXXXXX`).

#### Example:
```bash
python [Location.py](http://_vscodecontentref_/0)

####install
pip install phonenumbers colorama