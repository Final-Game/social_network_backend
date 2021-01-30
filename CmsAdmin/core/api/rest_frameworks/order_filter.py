from rest_framework.filters import OrderingFilter


class CustomOrderingFilter(OrderingFilter):
    def get_ordering(self, request, queryset, view):
        """
        Ordering is set by a comma delimited ?ordering=... query parameter.

        The `ordering` query parameter can be overridden by setting
        the `ordering_param` value on the OrderingFilter or by
        specifying an `ORDERING_PARAM` value in the API settings.
        """
        params = request.query_params.get(self.ordering_param)
        if params:
            fields = [param.strip() for param in params.split(",")]

            if hasattr(view, "get_serializer_class"):
                try:
                    serializer_class = view.get_serializer_class()
                except AssertionError:
                    serializer_class = None

            else:
                serializer_class = getattr(view, "serializer_class", None)

            if serializer_class is not None:
                # get mapping fields allowed
                mapping_fields = [
                    field
                    for field_name, field in serializer_class().fields.items()
                    if field.source
                    in getattr(view, "ordering_fields", self.ordering_fields)
                ]

                for idx, f in enumerate(fields):
                    for field in mapping_fields:
                        if field.field_name in f:
                            fields[idx] = f.replace(field.field_name, field.source)

            ordering = self.remove_invalid_fields(queryset, fields, view, request)
            if ordering:
                return ordering

        # No ordering was included, or all the ordering fields were invalid
        return self.get_default_ordering(view)
