from setuptools import setup, find_packages

install_requires = [
        'setuptools',
        'Django',
        'yos_social_sdk',
]

dependency_links = [
        'http://pypi.saaskit.org/yos-social-sdk/',
        'http://dist.repoze.org',
]
 
setup(name="saaskit-yql",
           version="0.1",
           description="Django application supporting YQL",
           author="CrowdSense",
           author_email="admin@crowdsense.com",
           packages=find_packages(),
           include_package_data=True,
           install_requires = install_requires,
           entry_points="""
           # -*- Entry points: -*-
           """,
           dependency_links =  dependency_links,
)
