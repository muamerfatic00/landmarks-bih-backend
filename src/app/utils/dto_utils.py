def to_dto(dto_class, obj):
    return dto_class.model_validate(obj)