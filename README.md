# HA Awtrix

This component uses the MQTT API of [Awtrix](https://blueforcer.github.io/awtrix3/#/) in Home Assistant easily by adding several additional actions.

## Installation

### HACS

You can add the component automatically using HACS by clicking the following link:

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=miguelangellv&repository=ha-awtrix&category=integration)

### Manual

You can install the component manually by copying the contents of the `custom_components/ha_awtrix` folder into the `custom_components` folder of your configuration.

## Configuration

Once installed, go to _Devices and Services -> Add Integration_ and search for _Awtrix_. After adding it, you will have the new actions available.

## Actions

### Awtrix Settings

The `awtrix.settings` action allows you to configure various parameters of the Awtrix display, such as brightness, clock settings, enabling and disabling applications, etc.

### Awtrix Notification

The `awtrix.notification` action allows you to send notifications to the Awtrix display. It has many options to customize the notification according to your needs.

### Awtrix Custom APP

The `awtrix.custom_app` action allows you to create and update custom Awtrix applications. You can create custom applications with various elements such as text, icons, etc.
