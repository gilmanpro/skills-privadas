# Tipos, Enums y Eventos de Flet

## Enums principales

| Enum | Valores clave |
|------|---------------|
| `ThemeMode` | `SYSTEM`, `LIGHT`, `DARK` |
| `MainAxisAlignment` | `START`, `END`, `CENTER`, `SPACE_BETWEEN`, `SPACE_AROUND`, `SPACE_EVENLY` |
| `CrossAxisAlignment` | `START`, `END`, `CENTER`, `STRETCH`, `BASELINE` |
| `ScrollMode` | `ADAPTIVE`, `ALWAYS`, `AUTO`, `DRAGGING`, `HIDDEN`, `NONE` |
| `TextAlign` | `LEFT`, `RIGHT`, `CENTER`, `JUSTIFY`, `START`, `END` |
| `TextOverflow` | `CLIP`, `ELLIPSIS`, `FADE`, `VISIBLE` |
| `FontWeight` | `W_100` a `W_900`, `NORMAL`, `BOLD` |
| `TextThemeStyle` | `DISPLAY_LARGE`, `DISPLAY_MEDIUM`, `DISPLAY_SMALL`, `HEADLINE_LARGE`, `HEADLINE_MEDIUM`, `HEADLINE_SMALL`, `TITLE_LARGE`, `TITLE_MEDIUM`, `TITLE_SMALL`, `LABEL_LARGE`, `LABEL_MEDIUM`, `LABEL_SMALL`, `BODY_LARGE`, `BODY_MEDIUM`, `BODY_SMALL` |
| `TextDecoration` | `NONE`, `UNDERLINE`, `OVERLINE`, `LINE_THROUGH` |
| `TextDecorationStyle` | `SOLID`, `DOUBLE`, `DOTTED`, `DASHED`, `WAVY` |
| `BoxShape` | `RECTANGLE`, `CIRCLE` |
| `BoxFit` | `NONE`, `CONTAIN`, `COVER`, `FILL`, `FIT_HEIGHT`, `FIT_WIDTH`, `SCALE_DOWN` |
| `ImageRepeat` | `NO_REPEAT`, `REPEAT`, `REPEAT_X`, `REPEAT_Y` |
| `BorderStyle` | `NONE`, `SOLID` |
| `ClipBehavior` | `NONE`, `ANTI_ALIAS`, `ANTI_ALIAS_WITH_SAVE_LAYER`, `HARD_EDGE` |
| `BlendMode` | `CLEAR`, `COLOR`, `COLOR_BURN`, `COLOR_DODGE`, `DARKEN`, `DIFFERENCE`, `DST`, `DST_ATOP`, `DST_IN`, `DST_OUT`, `DST_OVER`, `EXCLUSION`, `HARD_LIGHT`, `HUE`, `LIGHTEN`, `LUMINOSITY`, `MODULATE`, `MULTIPLY`, `OVERLAY`, `PLUS`, `SATURATION`, `SCREEN`, `SOFT_LIGHT`, `SRC`, `SRC_ATOP`, `SRC_IN`, `SRC_OUT`, `SRC_OVER`, `VALUES`, `XOR` |
| `AnimationCurve` | `LINEAR`, `EASE`, `EASE_IN`, `EASE_OUT`, `EASE_IN_OUT`, `BOUNCE_IN`, `BOUNCE_OUT`, `BOUNCE_IN_OUT`, `DECELERATE`, `FAST_LINEAR_TO_SLOW_EASE`, `FAST_OUT_SLOW_IN`, `SLOW_MIDDLE`, `SPRING`, `ELASTIC_IN`, `ELASTIC_OUT`, `ELASTIC_IN_OUT` |
| `KeyboardType` | `TEXT`, `MULTILINE`, `NUMBER`, `PHONE`, `DATETIME`, `EMAIL`, `URL`, `VISIBLE_PASSWORD`, `STREET_ADDRESS`, `NAME`, `NONE` |
| `TextCapitalization` | `NONE`, `CHARACTERS`, `WORDS`, `SENTENCES` |
| `InputBorder` | `NONE`, `OUTLINE`, `UNDERLINE` |
| `NavigationBarLabelBehavior` | `ALWAYS_SHOW`, `ALWAYS_HIDE`, `ONLY_SHOW_SELECTED` |
| `NavigationRailLabelType` | `NONE`, `ALWAYS`, `ONLY_SHOW_SELECTED` |
| `DismissDirection` | `HORIZONTAL`, `VERTICAL`, `END_TO_START`, `START_TO_END`, `UP`, `DOWN` |
| `TabAlignment` | `START`, `CENTER`, `FILL` |
| `TabIndicatorAnimation` | `LINEAR`, `FADE` |
| `TabBarIndicatorSize` | `TAB`, `LABEL` |
| `AppView` | `FLET_APP`, `FLET_APP_WEB`, `FLET_APP_HIDDEN` |
| `WindowEventType` | `CLOSE`, `FOCUS`, `BLUR`, `MOVE`, `RESIZE`, `MAXIMIZE`, `UNMAXIMIZE`, `MINIMIZE`, `RESTORE`, `ENTER_FULL_SCREEN`, `LEAVE_FULL_SCREEN`, `RESIZE_END` |
| `PagePlatform` | `ANDROID`, `IOS`, `LINUX`, `MACOS`, `WINDOWS`, `WEB` |
| `DeviceOrientation` | `PORTRAIT_UP`, `PORTRAIT_DOWN`, `LANDSCAPE_LEFT`, `LANDSCAPE_RIGHT` |
| `Brightness` | `LIGHT`, `DARK` |
| `AppLifecycleState` | `SHOW`, `RESUME`, `HIDE`, `PAUSE`, `RESTART`, `DETACH` |
| `AppLifecycleStateChangeEvent` | `state: AppLifecycleState` |
| `PointerDeviceType` | `TOUCH`, `MOUSE`, `STYLUS`, `INVERTED_STYLUS`, `TRACKPAD`, `UNKNOWN` |
| `MouseCursor` | `ALIAS`, `ALL_SCROLL`, `BASIC`, `CELL`, `CLICK`, `CONTEXT_MENU`, `COPY`, `DISAPPEARING`, `FORBIDDEN`, `GRAB`, `GRABBING`, `HELP`, `MOVE`, `NO_DROP`, `NONE`, `PRECISE`, `PROGRESS`, `RESIZE_COLUMN`, `RESIZE_DOWN`, `RESIZE_DOWN_LEFT`, `RESIZE_DOWN_RIGHT`, `RESIZE_LEFT`, `RESIZE_LEFT_RIGHT`, `RESIZE_RIGHT`, `RESIZE_ROW`, `RESIZE_UP`, `RESIZE_UP_DOWN`, `RESIZE_UP_LEFT`, `RESIZE_UP_LEFT_DOWN_RIGHT`, `RESIZE_UP_RIGHT`, `RESIZE_UP_RIGHT_DOWN_LEFT`, `TEXT`, `WAIT`, `ZOOM_IN`, `ZOOM_OUT` |
| `StrokeCap` | `BUTT`, `ROUND`, `SQUARE` |
| `StrokeJoin` | `BEVEL`, `MITER`, `ROUND` |
| `PaintingStyle` | `FILL`, `STROKE` |
| `PointMode` | `CIRCLES`, `POINTS` |
| `GradientTileMode` | `CLAMP`, `MIRROR`, `REPEAT`, `DECAL` |
| `BlurTileMode` | `CLAMP`, `MIRROR`, `REPEAT`, `DECAL` |
| `FilterQuality` | `NONE`, `LOW`, `MEDIUM`, `HIGH` |
| `VisualDensity` | `STANDARD`, `COMPACT`, `COMFORTABLE` |
| `SnackBarBehavior` | `FIXED`, `FLOATING` |
| `OverlayVisibilityMode` | `ALWAYS`, `NEVER`, `EDITING` |
| `ContextMenuTrigger` | `PRIMARY_CLICK`, `SECONDARY_CLICK`, `LONG_PRESS` |
| `RouteUrlStrategy` | `PATH`, `HASH` |
| `StackFit` | `LOOSE`, `EXPAND`, `PASSTHROUGH` |
| `LabelPosition` | `ABOVE`, `BELOW` |
| `SliderInteraction` | `SLIDE_THUMB`, `SLIDE_TRACK`, `TAP_AND_SLIDE` |
| `TileAffinity` | `LEADING`, `TRAILING` |
| `LaunchMode` | `PLATFORM_DEFAULT`, `EXTERNAL_APPLICATION`, `IN_APP_WEB_VIEW`, `IN_POPUP_WINDOW` |
| `UrlTarget` | `SELF`, `BLANK` |
| `ScrollBarOrientation` | `HORIZONTAL`, `VERTICAL` |
| `ScrollKey` | `HOME`, `END`, `PAGE_UP`, `PAGE_DOWN` |
| `ScrollType` | `PIXEL`, `ITEM` |
| `SystemOverlayStyle` | `LIGHT`, `DARK` |
| `Locale` | `language_code`, `country_code`, `script_code` |
| `LocaleConfiguration` | `locales: list[Locale]` |
| `LocaleChangeEvent` | `locales: list[Locale]` |
| `ConnectivityType` | `BLUETOOTH`, `ETHERNET`, `MOBILE`, `WIFI`, `VPN`, `OTHER`, `NONE` |
| `BatteryState` | `CHARGING`, `DISCHARGING`, `FULL`, `CHARGED`, `EMPTY`, `UNKNOWN` |
| `AudioState` | `STOPPED`, `PLAYING`, `PAUSED`, `ERROR`, `LOADING`, `COMPLETED`, `IDLE` |
| `ReleaseMode` | `RELEASE`, `LOOP`, `STOP` |
| `AudioRecorderState` | `STOPPED`, `RECORDING`, `PAUSED`, `ERROR` |
| `AudioEncoder` | `AAC`, `AAC_LC`, `AAC_HE`, `AAC_HE_V2`, `AMR_NB`, `AMR_WB`, `FLAC`, `OPUS`, `OGG_OPUS`, `PCM_16BIT`, `WAV`, `WEBM`, `WEBM_OPUS` |
| `AndroidAudioSource` | `CAMCORDER`, `DEFAULT`, `MIC`, `REMOTE_SUBMIX`, `UNPROCESSED`, `VOICE_CALL`, `VOICE_COMMUNICATION`, `VOICE_DOWNLINK`, `VOICE_PERFORMANCE`, `VOICE_RECOGNITION`, `VOICE_UPLINK` |
| `GeolocatorPermissionStatus` | `DENIED`, `DENIED_FOREVER`, `GRANTED`, `LIMITED`, `PROVISIONAL`, `RESTRICTED`, `UNABLE_TO_DETERMINE`, `UNKNOWN` |
| `GeolocatorPositionAccuracy` | `LOWEST`, `LOW`, `MEDIUM`, `HIGH`, `HIGHEST`, `BEST`, `BEST_FOR_NAVIGATION`, `REDUCED` |
| `GeolocatorIOSActivityType` | `OTHER`, `AUTOMOTIVE_NAVIGATION`, `FITNESS`, `OTHER_NAVIGATION`, `AIRBORNE` |
| `PermissionStatus` | `DENIED`, `DENIED_FOREVER`, `GRANTED`, `LIMITED`, `PROVISIONAL`, `RESTRICTED`, `UNABLE_TO_DETERMINE`, `UNKNOWN` |
| `ShareResultStatus` | `SUCCESS`, `CANCELLED`, `ERROR` |
| `Assertiveness` | `POLITE`, `ASSERTIVE` |
| `WebBrowserName` | `CHROME`, `FIREFOX`, `SAFARI`, `EDGE`, `OPERA`, `SAMSUNG_INTERNET`, `UNKNOWN` |
| `WebRenderer` | `AUTO`, `CANVAS`, `HTML`, `SKIA` |
| `MarkdownExtensionSet` | `NONE`, `COMMON_MARK`, `GFM`, `GIT_HUB_FLAVORED` |
| `CodeLanguage` | `PYTHON`, `JAVASCRIPT`, `TYPESCRIPT`, `HTML`, `CSS`, `JSON`, `XML`, `YAML`, `MARKDOWN`, `SQL`, `JAVA`, `KOTLIN`, `SWIFT`, `CPP`, `C`, `CSHARP`, `RUST`, `GO`, `RUBY`, `PHP`, `DART`, `BASH`, `POWERSHELL`, `DIFF`, `PLAINTEXT` |
| `CodeTheme` | `DEFAULT`, `MONOKAI`, `MONOKAI_DIM`, `DRACULA`, `NORD`, `GITHUB`, `GITHUB_DARK`, `VSCODE`, `VSCODE_DARK`, `A11Y_DARK`, `A11Y_LIGHT`, `ATOM_ONE_DARK`, `ATOM_ONE_LIGHT`, `ONE_DARK_PRO`, `ONE_LIGHT`, `MATERIAL`, `MATERIAL_DARK`, `MATERIAL_LIGHT`, `SOLARIZED_DARK`, `SOLARIZED_LIGHT`, `TOKYO_NIGHT`, `TOKYO_NIGHT_STORM`, `TOKYO_NIGHT_LIGHT`, `NIGHT_OWL`, `NIGHT_OWL_LIGHT`, `POIMANDR`, `POIMANDR_DARK`, `POIMANDR_LIGHT`, `SETI`, `SETI_DARK`, `SETI_LIGHT`, `MIN_DARK`, `MIN_LIGHT`, `GRUVBOX_DARK`, `GRUVBOX_LIGHT`, `EVERFOREST_DARK`, `EVERFOREST_LIGHT`, `AURORA`, `AURORA_DARK`, `AURORA_LIGHT`, `NOCTIS_MINOR`, `NOCTIS_MINOR_DARK`, `NOCTIS_MINOR_LIGHT`, `KANAGAWA`, `KANAGAWA_DARK`, `KANAGAWA_LIGHT`, `LASERWAVE`, `LASERWAVE_DARK`, `LASERWAVE_LIGHT`, `FIREFLY`, `FIREFLY_DARK`, `FIREFLY_LIGHT`, `CUSTOM` |
| `CardVariant` | `ELEVATED`, `FILLED`, `OUTLINED` |
| `CupertinoDatePickerMode` | `DATE`, `TIME`, `DATE_AND_TIME`, `MONTH_YEAR`, `YEAR` |
| `CupertinoDatePickerDateOrder` | `DAY_MONTH_YEAR`, `MONTH_DAY_YEAR`, `YEAR_MONTH_DAY`, `YEAR_DAY_MONTH`, `DMY`, `MDY`, `YMD`, `YDM` |
| `CupertinoTimerPickerMode` | `HOUR_MINUTE`, `HOUR_MINUTE_SECOND`, `MINUTE_SECOND` |
| `CupertinoButtonSize` | `SMALL`, `MEDIUM`, `LARGE` |
| `DatePickerMode` | `DAY`, `YEAR` |
| `DatePickerEntryMode` | `CALENDAR`, `INPUT`, `CALENDAR_ONLY`, `INPUT_ONLY` |
| `TimePickerEntryMode` | `DIAL`, `INPUT`, `DIAL_ONLY`, `INPUT_ONLY` |
| `TimePickerHourFormat` | `HH`, `HH_MM`, `HH_MM_SS` |
| `PlaylistMode` | `NONE`, `SINGLE`, `LOOP`, `SHUFFLE` |
| `VideoControlsMode` | `NONE`, `DEFAULT`, `MATERIAL`, `MATERIAL_DESKTOP`, `ADAPTIVE` |
| `LogLevelSeverity` | `DEBUG`, `ERROR`, `INFO`, `VERBOSE`, `WARNING` |
| `RequestMethod` | `DELETE`, `GET`, `HEAD`, `OPTIONS`, `PATCH`, `POST`, `PUT` |
| `CameraLensDirection` | `BACK`, `FRONT`, `EXTERNAL` |
| `CameraLensType` | `BACK`, `FRONT`, `WIDE`, `ULTRA_WIDE`, `TELEPHOTO`, `MACRO`, `EXTERNAL` |
| `ExposureMode` | `AUTO`, `LOCKED` |
| `FlashMode` | `AUTO`, `ALWAYS`, `NEVER` |
| `FocusMode` | `AUTO`, `LOCKED` |
| `ResolutionPreset` | `LOW`, `MEDIUM`, `HIGH`, `VERY_HIGH`, `ULTRA_HIGH`, `MAX` |
| `ImageFormatGroup` | `JPEG`, `PNG`, `RAW`, `HEIF`, `HEVC` |
| `PrecisionType` | `PRECISE`, `ESTIMATED` |
| `PrivacyOptionsRequirementStatus` | `REQUIRED`, `NOT_REQUIRED`, `UNKNOWN` |
| `DebugGeography` | `DISABLED`, `EEA`, `NOT_EEA` |
| `ConsentStatus` | `NOT_REQUIRED`, `REQUIRED`, `OBTAINED`, `UNKNOWN` |
| `PaidEvent` | `revenue_usd_micros`, `currency_code`, `precision_type` |

## Clases de layout y decoración

| Clase | Props |
|-------|-------|
| `Alignment` | `x`, `y` (float, -1 a 1). Constantes: `TOP_LEFT`, `TOP_CENTER`, `TOP_RIGHT`, `CENTER_LEFT`, `CENTER`, `CENTER_RIGHT`, `BOTTOM_LEFT`, `BOTTOM_CENTER`, `BOTTOM_RIGHT` |
| `Offset` | `x`, `y` (float) |
| `Padding` | `left`, `top`, `right`, `bottom`. Métodos: `all(value)`, `symmetric(horizontal, vertical)`, `only(left, top, right, bottom)` |
| `Margin` | `left`, `top`, `right`, `bottom`. Métodos: `all(value)`, `symmetric(horizontal, vertical)`, `only(left, top, right, bottom)` |
| `Border` | `left`, `top`, `right`, `bottom` (BorderSide). Método: `all(width, color)` |
| `BorderSide` | `width`, `color`, `stroke_align` |
| `BorderRadius` | `top_left`, `top_right`, `bottom_left`, `bottom_right`. Métodos: `all(value)`, `only(top_left, top_right, bottom_left, bottom_right)`, `horizontal(top, bottom)`, `vertical(left, right)` |
| `BoxShadow` | `color`, `offset`, `blur_radius`, `spread_radius`, `blur_style` |
| `BoxDecoration` | `bgcolor`, `border`, `border_radius`, `shadow`, `gradient`, `image`, `shape` |
| `DecorationImage` | `src`, `fit`, `repeat`, `color_filter`, `alignment`, `border_radius`, `filter_quality`, `match_text_direction`, `opacity`, `center_slice`, `scale`, `flip_horizontally`, `flip_vertically`, `gapless_playback`, `error_builder` |
| `Gradient` | Base para `LinearGradient`, `RadialGradient`, `SweepGradient` |
| `LinearGradient` | `begin`, `end`, `colors`, `stops`, `tile_mode`, `rotation` |
| `RadialGradient` | `center`, `radius`, `colors`, `stops`, `tile_mode`, `focal`, `focal_radius` |
| `SweepGradient` | `center`, `start_angle`, `end_angle`, `colors`, `stops`, `rotation` |
| `Blur` | `sigma_x`, `sigma_y`, `tile_mode` |
| `ColorFilter` | `color`, `blend_mode` |
| `Animation` | `duration` (int ms), `curve` (AnimationCurve) |
| `AnimationStyle` | `duration`, `curve`, `reverse_duration` |
| `Rotate` | `angle`, `alignment` |
| `Scale` | `scale`, `scale_x`, `scale_y`, `alignment` |
| `Transform` | `rotate`, `scale`, `translate`, `matrix4`, `alignment`, `transform_hit_tests`, `filter_quality` |
| `Matrix4` | `values: list[float]` (16 elementos) |
| `Size` | `width`, `height` |
| `Rect` | `left`, `top`, `right`, `bottom` |
| `Duration` | `seconds`, `minutes`, `hours`, `days`, `microseconds`, `milliseconds` |
| `BoxConstraints` | `min_width`, `max_width`, `min_height`, `max_height` |
| `StrutStyle` | `font_family`, `font_size`, `height`, `leading`, `force_strut_height` |
| `TextStyle` | `size`, `color`, `bgcolor`, `weight`, `italic`, `font_family`, `decoration`, `decoration_color`, `decoration_style`, `decoration_thickness`, `letter_spacing`, `word_spacing`, `height`, `leading_distribution`, `locale`, `foreground`, `background`, `shadows`, `font_features`, `text_overflow`, `package`, `debug_label` |
| `TextSpan` | `text`, `style`, `spans`, `url`, `semantics_label`, `on_click`, `on_enter`, `on_exit` |
| `ButtonStyle` | `color`, `bgcolor`, `overlay_color`, `shadow_color`, `surface_tint_color`, `elevation`, `padding`, `side`, `shape`, `animation_duration`, `text_style`, `icon_color`, `icon_size`, `mouse_cursor`, `visual_density`, `enable_feedback` |
| `Theme` | `color_scheme_seed`, `color_scheme`, `text_theme`, `appbar_theme`, `badge_theme`, `banner_theme`, `bottom_appbar_theme`, `bottom_sheet_theme`, `button_theme`, `card_theme`, `checkbox_theme`, `chip_theme`, `data_table_theme`, `date_picker_theme`, `dialog_theme`, `divider_theme`, `dropdown_theme`, `expansion_tile_theme`, `filled_button_theme`, `floating_action_button_theme`, `icon_button_theme`, `icon_theme`, `list_tile_theme`, `navigation_bar_theme`, `navigation_drawer_theme`, `navigation_rail_theme`, `outlined_button_theme`, `popup_menu_theme`, `progress_indicator_theme`, `radio_theme`, `scrollbar_theme`, `search_bar_theme`, `search_view_theme`, `segmented_button_theme`, `slider_theme`, `snack_bar_theme`, `switch_theme`, `tab_bar_theme`, `text_button_theme`, `text_theme`, `time_picker_theme`, `tooltip_theme`, `use_material3` |
| `ColorScheme` | `primary`, `on_primary`, `primary_container`, `on_primary_container`, `secondary`, `on_secondary`, `secondary_container`, `on_secondary_container`, `tertiary`, `on_tertiary`, `tertiary_container`, `on_tertiary_container`, `error`, `on_error`, `error_container`, `on_error_container`, `background`, `on_background`, `surface`, `on_surface`, `surface_variant`, `on_surface_variant`, `outline`, `outline_variant`, `shadow`, `scrim`, `inverse_surface`, `inverse_on_surface`, `inverse_primary`, `surface_tint` |
| `TextTheme` | `display_large`, `display_medium`, `display_small`, `headline_large`, `headline_medium`, `headline_small`, `title_large`, `title_medium`, `title_small`, `label_large`, `label_medium`, `label_small`, `body_large`, `body_medium`, `body_small` |
| `PageTheme` | `bgcolor`, `padding`, `spacing`, `horizontal_alignment`, `vertical_alignment` |

## Eventos comunes

| Evento | Tipo | Data |
|--------|------|------|
| `ControlEvent` | `Event[T]` | `control`, `data`, `page`, `target` |
| `TapEvent` | `TapEvent[T]` | `x`, `y`, `global_x`, `global_y`, `kind` |
| `HoverEvent` | `HoverEvent[T]` | `x`, `y`, `global_x`, `global_y`, `kind` |
| `DragStartEvent` | `DragStartEvent[T]` | `x`, `y`, `global_x`, `global_y`, `kind` |
| `DragUpdateEvent` | `DragUpdateEvent[T]` | `x`, `y`, `global_x`, `global_y`, `dx`, `dy`, `kind` |
| `DragEndEvent` | `DragEndEvent[T]` | `x`, `y`, `global_x`, `global_y`, `kind`, `primary_velocity`, `velocity_x`, `velocity_y` |
| `ScaleStartEvent` | `ScaleStartEvent[T]` | `x`, `y`, `global_x`, `global_y`, `kind`, `pointer_count` |
| `ScaleUpdateEvent` | `ScaleUpdateEvent[T]` | `x`, `y`, `global_x`, `global_y`, `kind`, `pointer_count`, `scale`, `horizontal_scale`, `vertical_scale`, `rotation` |
| `ScaleEndEvent` | `ScaleEndEvent[T]` | `x`, `y`, `global_x`, `global_y`, `kind`, `pointer_count`, `velocity_x`, `velocity_y` |
| `KeyboardEvent` | `KeyboardEvent` | `key`, `shift`, `ctrl`, `alt`, `meta` |
| `KeyDownEvent` | `KeyDownEvent` | `key`, `shift`, `ctrl`, `alt`, `meta`, `repeat` |
| `KeyUpEvent` | `KeyUpEvent` | `key`, `shift`, `ctrl`, `alt`, `meta` |
| `KeyRepeatEvent` | `KeyRepeatEvent` | `key`, `shift`, `ctrl`, `alt`, `meta` |
| `RouteChangeEvent` | `RouteChangeEvent` | `route` |
| `ViewPopEvent` | `ViewPopEvent` | `view` |
| `WindowEvent` | `WindowEvent` | `type` (WindowEventType) |
| `ScrollEvent` | `ScrollEvent` | `x`, `y`, `min_x`, `max_x`, `min_y`, `max_y`, `direction`, `scroll_type` |
| `OnScrollEvent` | `OnScrollEvent` | `x`, `y`, `min_x`, `max_x`, `min_y`, `max_y`, `direction`, `scroll_type`, `scroll_delta_x`, `scroll_delta_y`, `scroll_velocity_x`, `scroll_velocity_y`, `overscroll` |
| `LongPressStartEvent` | `LongPressStartEvent[T]` | `x`, `y`, `global_x`, `global_y`, `kind` |
| `LongPressEndEvent` | `LongPressEndEvent[T]` | `x`, `y`, `global_x`, `global_y`, `kind`, `velocity_x`, `velocity_y` |
| `MultiTapEvent` | `MultiTapEvent[T]` | `x`, `y`, `global_x`, `global_y`, `kind`, `count` |
| `DragTargetEvent` | `DragTargetEvent[T]` | `x`, `y`, `global_x`, `global_y`, `kind`, `data` |
| `DragTargetLeaveEvent` | `DragTargetLeaveEvent[T]` | `x`, `y`, `global_x`, `global_y`, `kind` |
| `DragWillAcceptEvent` | `DragWillAcceptEvent[T]` | `x`, `y`, `global_x`, `global_y`, `kind`, `data` |
| `DismissibleDismissEvent` | `DismissibleDismissEvent[T]` | `direction` |
| `DismissibleUpdateEvent` | `DismissibleUpdateEvent[T]` | `direction`, `reached`, `previous_reached` |
| `FilePickerFile` | `FilePickerFile` | `name`, `path`, `size`, `relative_path` |
| `FilePickerUploadEvent` | `FilePickerUploadEvent` | `file_name`, `progress`, `error` |
| `FilePickerResultEvent` | `FilePickerResultEvent` | `files`, `path` |
| `LoginEvent` | `LoginEvent` | `error`, `user` |
| `PageMediaData` | `PageMediaData` | `orientation`, `width`, `height`, `device_pixel_ratio`, `padding`, `view_padding`, `view_insets`, `system_bottom_bar_height`, `system_left_bar_width`, `system_right_bar_width`, `system_top_bar_height` |
| `PageResizeEvent` | `PageResizeEvent` | `width`, `height` |
| `LayoutSizeChangeEvent` | `LayoutSizeChangeEvent[T]` | `width`, `height`, `old_width`, `old_height` |
| `TextSelectionChangeEvent` | `TextSelectionChangeEvent[T]` | `selection_start`, `selection_end`, `selection_text` |
| `OnReorderEvent` | `OnReorderEvent` | `start_index`, `old_start_index`, `new_index` |
| `ContextMenuSelectEvent` | `ContextMenuSelectEvent` | `control`, `data` |
| `ContextMenuDismissEvent` | `ContextMenuDismissEvent` | `control` |
| `DataColumnSortEvent` | `DataColumnSortEvent` | `column_index`, `ascending` |
| `ExpansionPanelListChangeEvent` | `ExpansionPanelListChangeEvent` | `panel_index` |
| `TabBarHoverEvent` | `TabBarHoverEvent` | `index` |
| `AutoCompleteSelectEvent` | `AutoCompleteSelectEvent` | `selection` |
| `AutoCompleteSuggestion` | `AutoCompleteSuggestion` | `key`, `value` |
| `BatteryStateChangeEvent` | `BatteryStateChangeEvent` | `state` (BatteryState) |
| `ConnectivityChangeEvent` | `ConnectivityChangeEvent` | `type` (ConnectivityType) |
| `PlatformBrightnessChangeEvent` | `PlatformBrightnessChangeEvent` | `brightness` (Brightness) |
| `ScreenBrightnessChangeEvent` | `ScreenBrightnessChangeEvent` | `brightness` (float) |
| `AudioStateChangeEvent` | `AudioStateChangeEvent` | `state` (AudioState) |
| `AudioPositionChangeEvent` | `AudioPositionChangeEvent` | `position` (int) |
| `AudioDurationChangeEvent` | `AudioDurationChangeEvent` | `duration` (int) |
| `AudioRecorderStateChangeEvent` | `AudioRecorderStateChangeEvent` | `state` (AudioRecorderState) |
| `AudioRecorderStreamEvent` | `AudioRecorderStreamEvent` | `data` (bytes) |
| `AudioRecorderUploadEvent` | `AudioRecorderUploadEvent` | `progress`, `done`, `error`, `url` |
| `GeolocatorPositionChangeEvent` | `GeolocatorPositionChangeEvent` | `position` (GeolocatorPosition) |
| `SensorErrorEvent` | `SensorErrorEvent` | `error_code` |
| `AccelerometerReadingEvent` | `AccelerometerReadingEvent` | `x`, `y`, `z` |
| `GyroscopeReadingEvent` | `GyroscopeReadingEvent` | `x`, `y`, `z` |
| `MagnetometerReadingEvent` | `MagnetometerReadingEvent` | `x`, `y`, `z` |
| `UserAccelerometerReadingEvent` | `UserAccelerometerReadingEvent` | `x`, `y`, `z` |
| `BarometerReadingEvent` | `BarometerReadingEvent` | `pressure` |
| `SecureStorageEvent` | `SecureStorageEvent` | `key`, `value`, `action` |
| `ShareResult` | `ShareResult` | `status` (ShareResultStatus) |
| `MultiViewAddEvent` | `MultiViewAddEvent` | `view_id`, `data` |
| `MultiViewRemoveEvent` | `MultiViewRemoveEvent` | `view_id` |
| `ViewsPopUntilEvent` | `ViewsPopUntilEvent` | `route`, `result` |
| `WebViewConsoleMessageEvent` | `WebViewConsoleMessageEvent` | `message`, `level` (LogLevelSeverity) |
| `WebViewJavaScriptEvent` | `WebViewJavaScriptEvent` | `message` |
| `WebViewScrollEvent` | `WebViewScrollEvent` | `x`, `y` |
| `CameraImageEvent` | `CameraImageEvent` | `bytes`, `width`, `height`, `format` (ImageFormatGroup) |
| `CameraStateEvent` | `CameraStateEvent` | `available`, `permission` |
| `CanvasResizeEvent` | `CanvasResizeEvent` | `width`, `height`, `old_width`, `old_height` |
| `MapEvent` | `MapEvent` | `source`, `type`, `lat`, `lng`, `zoom`, `min_zoom`, `max_zoom`, `rotation`, `tilt` |
| `MapHoverEvent` | `MapHoverEvent` | `lat`, `lng`, `source` |
| `MapPointerEvent` | `MapPointerEvent` | `lat`, `lng`, `source`, `kind` |
| `MapPositionChangeEvent` | `MapPositionChangeEvent` | `lat`, `lng`, `zoom`, `source` |
| `MapTapEvent` | `MapTapEvent` | `lat`, `lng`, `source`, `kind` |
| `ChartEvent` | `ChartEvent` | `type` (ChartEventType), `bar_index`, `spot_index`, `section_index`, `data_point_index` |
| `ChartEventType` | `ChartEventType` | `BAR_TOUCH`, `BAR_ENTER`, `BAR_EXIT`, `LINE_TOUCH`, `LINE_ENTER`, `LINE_EXIT`, `PIE_TOUCH`, `PIE_ENTER`, `PIE_EXIT`, `SCATTER_TOUCH`, `SCATTER_ENTER`, `SCATTER_EXIT`, `CANDLESTICK_TOUCH`, `CANDLESTICK_ENTER`, `CANDLESTICK_EXIT`, `RADAR_TOUCH`, `RADAR_ENTER`, `RADAR_EXIT` |
| `BarChartEvent` | `BarChartEvent` | `type`, `group_index`, `rod_index`, `stack_item_index` |
| `LineChartEvent` | `LineChartEvent` | `type`, `data_point_index`, `spot_index` |
| `PieChartEvent` | `PieChartEvent` | `type`, `section_index` |
| `ScatterChartEvent` | `ScatterChartEvent` | `type`, `spot_index` |
| `CandlestickChartEvent` | `CandlestickChartEvent` | `type`, `spot_index` |
| `RadarChartEvent` | `RadarChartEvent` | `type`, `data_set_index`, `entry_index` |

## Excepciones
| Excepción | Descripción |
|-----------|-------------|
| `FletException` | Base para excepciones de Flet |
| `FletPageDisconnectedException` | La página se desconectó |
| `FletUnimplementedPlatformException` | Funcionalidad no disponible en esta plataforma |
| `FletUnsupportedPlatformException` | Plataforma no soportada para esta operación |

## Hooks y utilidades (declarativo)
| Función | Descripción |
|---------|-------------|
| `@ft.component` | Decorador para crear componentes reutilizables |
| `@ft.control` | Decorador para crear controles personalizados |
| `@ft.view` | Decorador para definir vistas |
| `use_state(initial)` | Hook de estado (similar a React) |
| `use_effect(callback, deps)` | Hook de efectos secundarios |
| `use_ref(initial)` | Hook para referencia mutable |
| `use_callback(fn, deps)` | Hook para memoizar callbacks |
| `use_memo(fn, deps)` | Hook para memoizar valores |
| `use_context(context)` | Hook para acceder al contexto |
| `use_dialog()` | Hook para manejar diálogos |
| `use_route_params()` | Hook para parámetros de ruta |
| `use_route_location()` | Hook para ubicación de ruta |
| `use_route_loader_data()` | Hook para datos cargados de ruta |
| `use_route_outlet()` | Hook para outlet de ruta |
| `use_view_path()` | Hook para path de vista |
| `is_route_active(route)` | Verifica si una ruta está activa |
| `create_context(default)` | Crea un contexto |
| `Context` | Objeto contexto para pasar datos entre componentes |
| `Observable` | Clase para crear valores observables |
| `observable_decorator` | Decorador para hacer propiedades observables |
| `Ref` | Referencia a un control (`ft.Ref[T]()`) |
| `Component` | Clase base para componentes declarativos |
| `Value` | Clase para valores reactivos |
| `ValueKey` | Clave para valores reactivos |
| `DataChannel` | Canal de datos entre sesiones |
| `DataChannelOpenEvent` | Evento de apertura de canal de datos |
| `Memo` | Clase para memoización |
| `Run` | Función para ejecutar código |
| `RunAsync` | Función para ejecutar código asíncrono |

## Colores
Usar `ft.Colors.NOMBRE`. Cientos de colores predefinidos: `RED`, `PINK`, `PURPLE`, `DEEP_PURPLE`, `INDIGO`, `BLUE`, `LIGHT_BLUE`, `CYAN`, `TEAL`, `GREEN`, `LIGHT_GREEN`, `LIME`, `YELLOW`, `AMBER`, `ORANGE`, `DEEP_ORANGE`, `BROWN`, `GREY`, `BLUE_GREY`, `BLACK`, `WHITE`, `TRANSPARENT`, con variantes `_50`, `_100`, ... `_900`, `_A100`, `_A200`, `_A400`, `_A700`.

Colores semánticos: `PRIMARY`, `ON_PRIMARY`, `PRIMARY_CONTAINER`, `ON_PRIMARY_CONTAINER`, `SECONDARY`, `ON_SECONDARY`, `SECONDARY_CONTAINER`, `ON_SECONDARY_CONTAINER`, `TERTIARY`, `ON_TERTIARY`, `TERTIARY_CONTAINER`, `ON_TERTIARY_CONTAINER`, `ERROR`, `ON_ERROR`, `ERROR_CONTAINER`, `ON_ERROR_CONTAINER`, `BACKGROUND`, `ON_BACKGROUND`, `SURFACE`, `ON_SURFACE`, `SURFACE_VARIANT`, `ON_SURFACE_VARIANT`, `OUTLINE`, `OUTLINE_VARIANT`, `SHADOW`, `SCRIMM`, `INVERSE_SURFACE`, `INVERSE_ON_SURFACE`, `INVERSE_PRIMARY`, `SURFACE_TINT`.

## Iconos
Usar `ft.Icons.NOMBRE`. Miles de iconos Material Design predefinidos. Ejemplos: `HOME`, `ADD`, `DELETE`, `EDIT`, `SEARCH`, `SETTINGS`, `PERSON`, `STAR`, `FAVORITE`, `MENU`, `CLOSE`, `ARROW_BACK`, `ARROW_FORWARD`, `CHECK`, `CLEAR`, `INFO`, `WARNING`, `ERROR`, `PHONE`, `EMAIL`, `LOCATION_ON`, `DATE_RANGE`, `ACCESS_TIME`, `PHOTO_CAMERA`, `VIDEOCAM`, `MUSIC_NOTE`, `PLAY_ARROW`, `PAUSE`, `STOP`, `SHARE`, `DOWNLOAD`, `UPLOAD`, `REFRESH`, `MORE_VERT`, `MORE_HORIZ`.

## Cupertino Icons
Usar `ft.CupertinoIcons.NOMBRE`. Ejemplos: `BACK`, `FORWARD`, `UP_ARROW`, `DOWN_ARROW`, `SHARE`, `SEARCH`, `SETTINGS`, `PERSON`, `STAR`, `HEART`, `PHONE`, `MAIL`, `MESSAGE`, `CAMERA`, `PHOTO`, `MUSIC_NOTE`, `PLAY`, `PAUSE`, `STOP`, `REFRESH`, `MORE`, `CLOSE`, `CHECKMARK`, `INFO`, `WARNING`, `HOME`, `BOOKMARK`, `BELL`, `CLOCK`, `CALENDAR`, `LOCATION`, `BATTERY_CHARGING`, `BATTERY_25`, `BATTERY_50`, `BATTERY_75`, `BATTERY_100`, `WIFI`, `CELLULAR`, `BLUETOOTH`, `AIRPLANE`, `FLASHLIGHT_ON`, `FLASHLIGHT_OFF`.