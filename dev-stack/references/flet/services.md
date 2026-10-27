# Servicios Nativos de Flet

## Cómo usar servicios
Los servicios se usan como controles independientes. Ejemplo:
```python
clipboard = ft.Clipboard()
page.overlay.append(clipboard)
page.update()
await clipboard.set_text_async("texto")
texto = await clipboard.get_text_async()
```

## Catálogo de Servicios

| Servicio | Props/Config | Métodos clave | Eventos |
|----------|-------------|---------------|---------|
| `Clipboard` | — | `get_text()`, `set_text(value)` | — |
| `FilePicker` | `file_type`, `allowed_extensions`, `allow_multiple`, `allow_any_file`, `dialog_title`, `initial_directory`, `file_name`, `upload` | `pick_files()`, `save_file()`, `get_directory_path()` | `on_result`, `on_upload` |
| `Audio` | `src`, `autoplay`, `volume`, `balance`, `playback_rate`, `release_mode` | `play()`, `pause()`, `resume()`, `seek(position)`, `get_duration()`, `get_current_position()`, `set_volume()`, `set_playback_rate()`, `set_balance()` | `on_loaded`, `on_duration_change`, `on_position_change`, `on_state_change`, `on_seek_complete` |
| `AudioRecorder` | `configuration`, `upload_settings` | `start()`, `stop()`, `pause()`, `resume()`, `cancel()`, `dispose()`, `is_recording()`, `get_state()`, `start_stream()`, `stop_stream()` | `on_state_change`, `on_stream`, `on_upload` |
| `UrlLauncher` | — | `launch_url(url)`, `can_launch_url(url)`, `close_in_app_web_view()` | — |
| `Share` | — | `share(text)`, `share_files(files)`, `share_with_result(text)`, `share_files_with_result(files)` | — |
| `SecureStorage` | — | `set(key, value)`, `get(key)`, `contains_key(key)`, `delete(key)`, `delete_all()`, `read_all()` | — |
| `SharedPreferences` | — | `set(key, value)`, `get(key)`, `contains_key(key)`, `remove(key)`, `clear()` | — |
| `StoragePaths` | — | `get_app_data_path()`, `get_cache_path()`, `get_downloads_path()`, `get_documents_path()`, `get_support_path()`, `get_temp_path()`, `get_trash_path()`, `get_app_config_path()` | — |
| `PermissionHandler` | — | `request_permission(permission)`, `check_permission(permission)`, `open_app_settings()` | — |
| `Geolocator` | `configuration` | `get_current_position()`, `get_last_known_position()`, `get_position_stream()`, `is_location_service_enabled()`, `open_location_settings()` | `on_position_change` |
| `Connectivity` | — | `get_connectivity_type()` | `on_change` |
| `Battery` | — | `get_battery_state()` | `on_state_change` |
| `Accelerometer` | — | `accelerometer_event_stream()` | `on_reading` |
| `Gyroscope` | — | `gyroscope_event_stream()` | `on_reading` |
| `Magnetometer` | — | `magnetometer_event_stream()` | `on_reading` |
| `UserAccelerometer` | — | `user_accelerometer_event_stream()` | `on_reading` |
| `Barometer` | — | `barometer_event_stream()` | `on_reading` |
| `ScreenBrightness` | — | `get_screen_brightness()`, `set_screen_brightness(brightness)` | `on_change` |
| `HapticFeedback` | — | `vibrate()`, `click()`, `heavy_click()`, `light_click()`, `medium_click()`, `selection_click()`, `wait()` | — |
| `ShakeDetector` | — | — | `on_shake` |
| `Wakelock` | — | `enable()`, `disable()`, `is_enabled()` | — |
| `Flashlight` | — | `turn_on()`, `turn_off()`, `is_available()` | — |
| `SemanticsService` | — | `announce(message, assertiveness)` | — |
| `BrowserContextMenu` | — | `disable()`, `enable()` | — |

## Tipos de permisos (PermissionHandler)
`Permission.ACCESS_CAMERA`, `Permission.ACCESS_FINE_LOCATION`, `Permission.ACCESS_COARSE_LOCATION`, `Permission.ACCESS_BACKGROUND_LOCATION`, `Permission.ACCESS_MEDIA_LOCATION`, `Permission.ACCESS_NOTIFICATION_POLICY`, `Permission.ACCESS_WIFI_STATE`, `Permission.ACCOUNT_MANAGER`, `Permission.ACTIVITY_RECOGNITION`, `Permission.ADD_VOICEMAIL`, `Permission.ANSWER_PHONE_CALLS`, `Permission.BLUETOOTH`, `Permission.BLUETOOTH_ADMIN`, `Permission.BLUETOOTH_ADVERTISE`, `Permission.BLUETOOTH_CONNECT`, `Permission.BLUETOOTH_SCAN`, `Permission.BODY_SENSORS`, `Permission.BODY_SENSORS_BACKGROUND`, `Permission.CALL_PHONE`, `Permission.CAMERA`, `Permission.CHANGE_NETWORK_STATE`, `Permission.CHANGE_WIFI_MULTICAST_STATE`, `Permission.CHANGE_WIFI_STATE`, `Permission.CLEAR_APP_CACHE`, `Permission.FLASHLIGHT`, `Permission.FOREGROUND_SERVICE`, `Permission.GET_ACCOUNTS`, `Permission.GET_PACKAGE_SIZE`, `Permission.INTERNET`, `Permission.KILL_BACKGROUND_PROCESSES`, `Permission.MANAGE_EXTERNAL_STORAGE`, `Permission.MANAGE_MEDIA`, `Permission.MEDIA_CONTENT_CONTROL`, `Permission.MODIFY_AUDIO_SETTINGS`, `Permission.NFC`, `Permission.NFC_PREFERRED_PAYMENT_INFO`, `Permission.NFC_TRANSACTION_EVENT`, `Permission.PACKAGE_USAGE_STATS`, `Permission.POST_NOTIFICATIONS`, `Permission.PROCESS_OUTGOING_CALLS`, `Permission.QUERY_ALL_PACKAGES`, `Permission.READ_CALENDAR`, `Permission.READ_CALL_LOG`, `Permission.READ_CONTACTS`, `Permission.READ_EXTERNAL_STORAGE`, `Permission.READ_HISTORY_BOOKMARKS`, `Permission.READ_INSTALL_SESSIONS`, `Permission.READ_LOGS`, `Permission.READ_MEDIA_AUDIO`, `Permission.READ_MEDIA_IMAGES`, `Permission.READ_MEDIA_VIDEO`, `Permission.READ_PHONE_NUMBERS`, `Permission.READ_PHONE_STATE`, `Permission.READ_PROFILE`, `Permission.READ_SMS`, `Permission.READ_SOCIAL_STREAM`, `Permission.READ_SYNC_SETTINGS`, `Permission.READ_SYNC_STATS`, `Permission.READ_USER_DICTIONARY`, `Permission.READ_VOICEMAIL`, `Permission.RECEIVE_BOOT_COMPLETED`, `Permission.RECEIVE_MMS`, `Permission.RECEIVE_SMS`, `Permission.RECEIVE_WAP_PUSH`, `Permission.RECORD_AUDIO`, `Permission.REQUEST_DELETE_PACKAGES`, `Permission.REQUEST_INSTALL_PACKAGES`, `Permission.SCHEDULE_EXACT_ALARM`, `Permission.SEND_SMS`, `Permission.SET_ALARM`, `Permission.SET_ALWAYS_FINISH`, `Permission.SET_ANIMATION_SCALE`, `Permission.SET_DEBUG_APP`, `Permission.SET_PROCESS_LIMIT`, `Permission.SET_TIME`, `Permission.SET_TIME_ZONE`, `Permission.SET_WALLPAPER`, `Permission.SET_WALLPAPER_HINTS`, `Permission.SMS_FINANCIAL_TRANSACTIONS`, `Permission.STATUS_BAR`, `Permission.SYSTEM_ALERT_WINDOW`, `Permission.TRANSMIT_IR`, `Permission.UNINSTALL_SHORTCUT`, `Permission.UNKNOWN`, `Permission.USE_BIOMETRIC`, `Permission.USE_FINGERPRINT`, `Permission.USE_FULL_SCREEN_INTENT`, `Permission.USE_SIP`, `Permission.UPDATE_PACKAGES_WITHOUT_USER_ACCESS`, `Permission.VIBRATE`, `Permission.WAKE_LOCK`, `Permission.WRITE_APN_SETTINGS`, `Permission.WRITE_CALENDAR`, `Permission.WRITE_CALL_LOG`, `Permission.WRITE_CONTACTS`, `Permission.WRITE_EXTERNAL_STORAGE`, `Permission.WRITE_GSERVICES`, `Permission.WRITE_HISTORY_BOOKMARKS`, `Permission.WRITE_PROFILE`, `Permission.WRITE_SECURE_SETTINGS`, `Permission.WRITE_SETTINGS`, `Permission.WRITE_SMS`, `Permission.WRITE_SYNC_SETTINGS`, `Permission.WRITE_USER_DICTIONARY`, `Permission.WRITE_VOICEMAIL`

## Configuración de AudioRecorder
```python
ft.AudioRecorderConfiguration(
    audio_source=ft.AndroidAudioSource.MIC,
    output_format=ft.AudioEncoder.AAC,
    sample_rate=44100,
    channels=2,
    bit_rate=128000,
)
```

## Configuración de Geolocator
```python
ft.GeolocatorConfiguration(
    location_accuracy=ft.GeolocatorPositionAccuracy.HIGH,
    distance_filter=0,
    time_limit=Duration(seconds=10),
)
```