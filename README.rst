=======
Configs
=======

Quick start
-----------

1. Add "polls" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'configs',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('', include('configs.urls')),
