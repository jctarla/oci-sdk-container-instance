import oci
import logging


logging.getLogger('oci').setLevel(logging.DEBUG)

config = oci.config.from_file()  # Load the OCI configuration from a file
config['log_requests'] = True


my_image_url="gru.ocir.io/xxxxxx/xxxxxx:latest"
my_subnet_id="ocid1.subnet.oc1.sa-saopaulo-1.xxxxxq"
my_compartment_id="ocid1.compartment.oc1..axxxxx"

print("Starting")
# Initialize service client with default config file
container_instances_client = oci.container_instances.ContainerInstanceClient(config)

print("Config")
my_shape_config=oci.container_instances.models.CreateContainerInstanceShapeConfigDetails(
            ocpus=1.0,
            memory_in_gbs=1.0)

print("Containers")
my_containers=[oci.container_instances.models.CreateContainerDetails(
                image_url=my_image_url,
                display_name="ContainerFromSDK")]

print("VNICS")
my_vnics=[oci.container_instances.models.CreateContainerVnicDetails(
                subnet_id=my_subnet_id)]

print("Details instances")
instances_details=oci.container_instances.models.CreateContainerInstanceDetails(
        compartment_id=my_compartment_id,
        availability_domain="LNlm:SA-SAOPAULO-1-AD-1",
        shape="CI.Standard.E3.Flex",
        shape_config=my_shape_config,
        containers=my_containers,
        vnics=my_vnics,
        display_name="TesteContainerCreation",
        container_restart_policy="ON_FAILURE",
    )

print("GO")

create_container_instance_response = container_instances_client.create_container_instance(
    create_container_instance_details=instances_details
)
