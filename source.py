def add_url_rule(self, rule, endpoint=None, view_func=None, **options):
    """A helper method to register a rule (and optionally a view function)
    to the application.  The endpoint is automatically prefixed with the
    blueprint's name.
    """
    if self.url_prefix is not None:
        if rule:
            rule = "/".join((self.url_prefix.rstrip("/"), rule.lstrip("/")))
        else:
            rule = self.url_prefix
    options.setdefault("subdomain", self.subdomain)
    if endpoint is None:
        endpoint = _endpoint_from_view_func(view_func)
    defaults = self.url_defaults
    if "defaults" in options:
        defaults = dict(defaults, **options.pop("defaults"))
    self.app.add_url_rule(
        rule,
        f"{self.blueprint.name}.{endpoint}",
        view_func,
        defaults=defaults,
        **options,
    )
