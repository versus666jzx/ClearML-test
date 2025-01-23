from clearml import PipelineDecorator
from pipelines.pipeline_test import step_1, step_2, step_3


@PipelineDecorator.pipeline(
    name="pipeline",
    project="Pipeline Decorator",
    version="0.1",
    pipeline_execution_queue="default",
    default_queue="default"
)
def main():
    print("Starting pipeline")
    step_1.step_one()
    print("Finished step_1")
    step_2.step_two()
    print("Finished step_2")
    step_3.step_three()
    print("Finished step_3")


if __name__ == "__main__":
    main()
