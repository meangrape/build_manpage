import argparse

def get_parser():
    parser = argparse.ArgumentParser(prog='example', description='Manage EC2 example instances', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-i', '--iam', type=str, metavar='IAMID', 
        help='Your IAM id. We attempt to read an IAM_ID environemnt variable and fallback to your username. This is the primary key used to identify AWS resources belonging to you',
        )
    parser.add_argument('-v', '--version', action='version', version="example version 0.2.0")
    

    subparsers = parser.add_subparsers()
    parser_create = subparsers.add_parser('create', help='Create a example group (instance, keypair, security group)')
    parser_create.add_argument('-s', '--size', type=str, help='Instance size (micro or small)', default='micro')
    parser_create.add_argument('-c', '--client', type=str, help="Tag instance with this client's name (an arbitrary string)")
    parser_create.add_argument('-l', '--lifetime', type=int, help='Will stop in this many hours', default=12)

    parser_destroy = subparsers.add_parser('destroy', help='Destroy a example group and associated resources')
    destroy_group = parser_destroy.add_mutually_exclusive_group(required=True)
    destroy_group.add_argument('-a', '--all', action='store_true', help='Delete all of your examples and resources')
    destroy_group.add_argument('-c', '--client', type=str, help='Delete all of your instances with this client name')
    destroy_group.add_argument('-t', '--tag', type=str, help='Unique resource tag to be deleted')
    
    parser_inventory = subparsers.add_parser('inventory', help='List examples you have running in AWS')
    parser_inventory.add_argument('-d', '--detailed', action='store_true', help='Provide additional EC2 specific information')
    
    parser_stop = subparsers.add_parser('stop', help='Stop running instances')
    parser_stop.add_argument('-f', '--force', action='store_true', help='Force shutdown', default=False)
    stop_group = parser_stop.add_mutually_exclusive_group(required=True)
    stop_group.add_argument('-a', '--all', action='store_true', help='Stop (not terminate) all of your instances')
    stop_group.add_argument('-c', '--client', type=str, help='Stop (not terminate) all instances for this client')
    stop_group.add_argument('-t', '--tag', type=str, help='Unique resource tag to be stopped')

    parser_license = subparsers.add_parser('license', help="http://github.com/meangrape/build_manpage/LICENSE")
    return parser


def main():
    parser = get_parser() 
    args = parser.parse_args()


if __name__ == "__main__":
    main()
