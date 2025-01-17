from clearml.automation import TaskScheduler


scheduler = TaskScheduler()
scheduler.add_task(
    schedule_task_id='6ca3a30c48a64ff98dce068e96047273',  # pipeline id
    queue="default",
    name="Example sheduller",
    execute_immediately=True,
    minute=2,
    target_project="examples"
)

scheduler.start_remotely(queue="default")
