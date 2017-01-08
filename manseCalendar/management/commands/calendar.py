# -*- coding: utf-8 -*-

from django.core.management import BaseCommand

from manseCalendar.management.commands.mansecalendar import insert, letter


class Command(BaseCommand):

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.insert_subcommand = insert.Command()
        self.letter_subcommand = letter.Command()

    SUBCOMMAND_INSERT = 'insert'
    SUBCOMMAND_LETTER = 'letter'

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)
        subparsers = parser.add_subparsers(dest='subcommand', help='sub-command help')
        insert_parser = subparsers.add_parser(Command.SUBCOMMAND_INSERT, description='insert calendar data to Days model table')
        letter_parser = subparsers.add_parser(Command.SUBCOMMAND_LETTER, description='update letter properties in Days model table')
        # parser.add_argument('--insert', action='storeTrue', dest='insert', help='insert solar date and lunar date.')
        # parser.add_argument('--input', action='storeTrue', dest='input')
        # parser.add_argument('--letter', action='storeTrue', )

        self.insert_subcommand.add_arguments(insert_parser)
        self.letter_subcommand.add_arguments(letter_parser)

    def handle(self, *args, **options):
        mode = options['subcommand']
        if mode == Command.SUBCOMMAND_INSERT:
            cmd = self.insert_subcommand
        elif mode == Command.SUBCOMMAND_LETTER:
            cmd = self.letter_subcommand

        if cmd:
            return cmd.handle(*args, **options)

        raise Exception('unknown subcommand, %s' % mode)
