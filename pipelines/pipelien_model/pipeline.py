from clearml import PipelineDecorator
from time import sleep


@PipelineDecorator.pipeline(
    name="pipeline",
    project="Pipeline Decorator",
    version="0.1",
    pipeline_execution_queue="default",
    default_queue="default"
)
def main():
    print("Starting pipeline")
    sleep(1)
    print("Finished step_1")
    sleep(1)
    print("Finished step_2")
    sleep(1)
    print("Finished step_3")


if __name__ == "__main__":
    main()
