from alembic.operations import Operations, MigrateOperation


class ReplaceableObject:
    def __init__(self, name, sql_text, schema=None):
        self.name = name
        self.sql_text = sql_text
        self.schema = schema


class ReversibleOp(MigrateOperation):
    def __init__(self, target):
        self.target = target

    @classmethod
    def invoke_for_target(cls, operations, target):
        operation = cls(target)
        return operations.invoke(operation)

    def reverse(self):
        raise NotImplementedError()

    def to_diff_tuple(self):
        pass

    @classmethod
    def _get_object_from_version(cls, operations, ident):
        version, obj_name = ident.split(".")

        module = operations.get_context().script.get_revision(version).module
        obj = getattr(module, obj_name)
        return obj

    @classmethod
    def replace(cls, operations, target, replaces=None, replace_with=None):
        if replaces:
            old_obj = cls._get_object_from_version(operations, replaces)
            drop_old = cls(old_obj).reverse()
            create_new = cls(target)
        elif replace_with:
            old_obj = cls._get_object_from_version(operations, replace_with)
            drop_old = cls(target).reverse()
            create_new = cls(old_obj)
        else:
            raise TypeError("replaces or replace_with is required")

        operations.invoke(drop_old)
        operations.invoke(create_new)


@Operations.register_operation("create_view", "invoke_for_target")
@Operations.register_operation("replace_view", "replace")
class CreateViewOp(ReversibleOp):
    def reverse(self):
        return DropViewOp(self.target)


@Operations.register_operation("drop_view", "invoke_for_target")
class DropViewOp(ReversibleOp):
    def reverse(self):
        return CreateViewOp(self.target)


@Operations.register_operation("create_func", "invoke_for_target")
@Operations.register_operation("replace_func", "replace")
class CreateFuncOp(ReversibleOp):
    def reverse(self):
        return DropFuncOp(self.target)


@Operations.register_operation("drop_func", "invoke_for_target")
class DropFuncOp(ReversibleOp):
    def reverse(self):
        return CreateFuncOp(self.target)


@Operations.register_operation("create_sp", "invoke_for_target")
@Operations.register_operation("replace_sp", "replace")
class CreateSPOp(ReversibleOp):
    def reverse(self):
        return DropSPOp(self.target)


@Operations.register_operation("drop_sp", "invoke_for_target")
class DropSPOp(ReversibleOp):
    def reverse(self):
        return CreateSPOp(self.target)


@Operations.implementation_for(CreateViewOp)
def create_view(operations, operation):
    if operation.target.schema is not None:
        schema_cmd = f"set search_path to {operation.target.schema};"
        operations.execute(schema_cmd)
    operations.execute(
        f"""CREATE VIEW {operation.target.name} AS {operation.target.sql_text}"""
    )


@Operations.implementation_for(DropViewOp)
def drop_view(operations, operation):
    if operation.target.schema is not None:
        schema_cmd = f"set search_path to {operation.target.schema};"
        operations.execute(schema_cmd)
    operations.execute(f"""DROP VIEW {operation.target.name}""")


@Operations.implementation_for(CreateFuncOp)
def create_func(operations, operation):
    if operation.target.schema is not None:
        schema_cmd = f"set search_path to {operation.target.schema};"
        operations.execute(schema_cmd)
    operations.execute(operation.target.sql_text)


@Operations.implementation_for(DropFuncOp)
def drop_func(operations, operation):
    if operation.target.schema is not None:
        schema_cmd = f"set search_path to {operation.target.schema};"
        operations.execute(schema_cmd)
    operations.execute(f"""DROP FUNCTION {operation.target.name}""")


@Operations.implementation_for(CreateSPOp)
def create_sp(operations, operation):
    operations.execute(
        f"""CREATE FUNCTION {operation.target.name} {operation.target.sql_text}"""
    )


@Operations.implementation_for(DropSPOp)
def drop_sp(operations, operation):
    operations.execute(f"""DROP FUNCTION {operation.target.name}""")
