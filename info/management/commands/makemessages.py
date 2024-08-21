from django.core.management.commands import makemessages


class Command(makemessages.Command):
    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser.add_argument(
            "--extra-keyword",
            dest="xgettext_keywords",
            action="append",
        )

    def handle(self, *args, **options):
        xgettext_keywords = options.pop("xgettext_keywords")
        if xgettext_keywords:
            self.xgettext_options = makemessages.Command.xgettext_options[:] + [
                "--keyword=%s" % kwd for kwd in xgettext_keywords
            ]
        super().handle(*args, **options)