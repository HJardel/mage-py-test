from deltalake import DeltaTable
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_table(*args, **kwargs):
    """
    Load a Delta Table

    Docs: https://delta-io.github.io/delta-rs/python/usage.html#loading-a-delta-table
    """
    storage_options = {
        'AZURE_STORAGE_ACCOUNT_NAME': '',
        'AZURE_STORAGE_ACCOUNT_KEY': '',
        'AZURE_STORAGE_ACCESS_KEY': '',
        'AZURE_STORAGE_MASTER_KEY': '',
        'AZURE_STORAGE_CLIENT_ID': '',
        'AZURE_STORAGE_CLIENT_SECRET': '',
        'AZURE_STORAGE_TENANT_ID': '',
        'AZURE_STORAGE_SAS_KEY': '',
        'AZURE_STORAGE_TOKEN': '',
        'AZURE_STORAGE_USE_EMULATOR': '',
    }

    uri = 'az://[container]/[key]'

    dt = DeltaTable(uri, storage_options=storage_options)

    return dt.to_pandas()


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'