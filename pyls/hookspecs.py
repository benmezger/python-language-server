# Copyright 2017 Palantir Technologies, Inc.
# pylint: disable=redefined-builtin, unused-argument
from pyls import hookspec
from typing import List

from pyls.config import Config
from pyls.workspace import Workspace, Document


@hookspec
def pyls_code_actions(config: Config, workspace: Workspace, document: Document, range: dict, context: dict):
    pass


@hookspec
def pyls_code_lens(config: Config, workspace: Workspace, document: Document):
    pass


@hookspec
def pyls_commands(config: Config, workspace: Workspace) -> List[str]:
    """The list of command strings supported by the server.

    Returns:
        List[str]: The supported commands.
    """


@hookspec
def pyls_completions(config: Config, workspace: Workspace, document: Document, position: dict):
    pass


@hookspec
def pyls_definitions(config: Config, workspace: Workspace, document: Document, position: dict):
    pass


@hookspec
def pyls_dispatchers(config: Config, workspace: Workspace):
    pass


@hookspec
def pyls_document_did_open(config: Config, workspace: Workspace, document: Document):
    pass


@hookspec
def pyls_document_did_save(config: Config, workspace: Workspace, document: Document):
    pass


@hookspec
def pyls_document_highlight(config: Config, workspace: Workspace, document: Document, position: dict):
    pass


@hookspec
def pyls_document_symbols(config: Config, workspace: Workspace, document: Document):
    pass


@hookspec(firstresult=True)
def pyls_execute_command(config: Config, workspace: Workspace, command: str, arguments: list):
    pass


@hookspec
def pyls_experimental_capabilities(config: Config, workspace: Workspace):
    pass


@hookspec(firstresult=True)
def pyls_folding_range(config: Config, workspace: Workspace, document: Document):
    pass


@hookspec(firstresult=True)
def pyls_format_document(config: Config, workspace: Workspace, document: Document):
    pass


@hookspec(firstresult=True)
def pyls_format_range(config: Config, workspace: Workspace, document: Document, range: dict):
    pass


@hookspec(firstresult=True)
def pyls_hover(config: Config, workspace: Workspace, document: Document, position: dict):
    pass


@hookspec
def pyls_initialize(config: Config, workspace: Workspace):
    pass


@hookspec
def pyls_initialized():
    pass


@hookspec
def pyls_lint(config: Config, workspace: Workspace, document: Document, is_saved: bool):
    pass


@hookspec
def pyls_references(config: Config, workspace: Workspace, document: Document, position: dict,
                    exclude_declaration: dict):
    pass


@hookspec(firstresult=True)
def pyls_rename(config: Config, workspace: Workspace, document: Document, position: dict, new_name: str):
    pass


@hookspec
def pyls_settings(config: Config):
    pass


@hookspec(firstresult=True)
def pyls_signature_help(config: Config, workspace: Workspace, document: Document, position: dict):
    pass
