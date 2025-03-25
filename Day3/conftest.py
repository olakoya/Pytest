import pytest
from pytest_metadata.plugin import metadata_key

# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("Python", None) # pop means remove or delete
#     metadata.pop("Plugins", None)

def pytest_configuration(config): # For adding information hook isn't required
    config.stash[metadata_key]['Project Name'] = 'Parameterization'
    config.stash[metadata_key]['Module Name'] = 'test_Parameterization'
    config.stash[metadata_key]['Tester Name'] = 'Ola'
@pytest.mark.optionalhook
def pytest_metadata(metadata): # For modifying hook is required above
    metadata.pop("Python", None)  # pop means remove or delete
    metadata.pop("Plugins", None)