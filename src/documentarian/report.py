from pathlib import Path

import boto3
from langchain_aws import BedrockLLM
from langchain_core.prompts import PromptTemplate


report_prompt = """
You are an IT engineer investigating quality issues of the software your company
sells. Your job is to investigate an error and write an error resolution report
based on the resolution you found and the error logs where the issue occurred.

Write a coherent error resolution report using the error, resolution, and logs mentioned
below. Your error resolution report should mention the error encountered at the beginning.

error: {errors}
resolution: {resolutions}
logs: {error_log}

Error Encountered:
"""
report_template = PromptTemplate.from_template(report_prompt)

final_doc_template = """
{llm_res}

Full error logs:

{error_log}
"""


class ReportGenerator:

    def __init__(self, settings, ouptut_dir="data"):

        self.bedrock_client = boto3.client(
            "bedrock-runtime",
            region_name=settings.region,
            aws_access_key_id=settings.access_key,
            aws_secret_access_key=settings.secret_access_key
        )
        self.llm = BedrockLLM(
            client=self.bedrock_client,
            model_id="anthropic.claude-v2:1"
        )
        self.output_dir = Path().resolve().joinpath(ouptut_dir)

    def __call__(self, errors, resolutions, error_log, name_report):

        chain = (
            report_template
            | self.llm
        )

        prompt = PromptTemplate(input_variables=["errors", "resolutions", "error_log"], template=report_prompt)

        response = chain.invoke(
            {"errors": errors, "resolutions": resolutions, "error_log": error_log}
        )

        self.save_res(
            llm_res=response,
            error_log=error_log,
            name_report=name_report
        )

    
    def save_res(self, llm_res, error_log, name_report):

        final_doc = final_doc_template.format(
            llm_res=llm_res,
            error_log=error_log
        )

        tar_fp = self.output_dir.joinpath(name_report)

        with open(tar_fp, 'w', encoding='utf-8') as f:
            f.write(final_doc)
