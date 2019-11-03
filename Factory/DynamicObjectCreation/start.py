from network_connector import NetworkConnectorAdapter

adapter_type = input("Select an adapter type (HTTP or TCP): ")
adapter = NetworkConnectorAdapter.create(adapter_type)

adapter.connect()
