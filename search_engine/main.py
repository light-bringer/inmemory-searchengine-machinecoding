import organisation


def OrgFactory(name: str):
    return organisation.Org(name)


def main():
    org = OrgFactory('Org1')
    org.create_dataset('dataset1')
    org.insert_content('dataset1', 'i am a apple')
    org.insert_content('dataset1', 'i am a apple')
    org.insert_content('dataset1', 'i am a apple')
    org.insert_content('dataset1', 'i am an apple apple apple')
    org.insert_content('dataset1', 'i am an orange')
    org.insert_content('dataset1', 'i am an apple')
    org.search('dataset1', 'apple', 'count')
    org.search('dataset1', 'apple', 'timestamp')
    org.search('dataset1', 'grapes', 'timestamp')
    org.search('dataset1', 'orange', 'timestamp')
    org.search('dataset2', 'grapes', 'timestamp')


if __name__ == '__main__':
    main()
