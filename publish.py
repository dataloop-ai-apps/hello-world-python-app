import dtlpy as dl

if dl.token_expired():
    dl.login()

project = dl.projects.get(project_name="COCO ors")

# Publish your DPK
dpk = project.dpks.publish()

# Install or update the application
try:
    app = project.apps.get(app_name=dpk.display_name)
    app.dpk_version = dpk.version
    app.update()
except dl.exceptions.NotFound:
    print("installing ...")
    app = project.apps.install(dpk=dpk)


# Get the service
service = project.services.get("hello-world")

# Execute
dataset = project.datasets.get("your-dataset-name")
item = dataset.items.get(filepath="/turtle/7f90dea118.jpg")

execution = service.execute(
    function_name="hello_world",
    item_id=item.id,
    project_id=project.id,
)

# Wait for completion and get results
execution = execution.wait()
if execution.latest_status["status"] == "success":
    processed_item = execution.output
    print(f"Successfully processed item: {processed_item}")
else:
    print(f"Execution failed: {execution.latest_status['message']}")

# Get the updated item
item = dataset.items.get(item_id=item.id)
print(f"Updated item's metadata: {item.metadata.get('user')}")
