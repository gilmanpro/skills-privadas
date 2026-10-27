# Catálogo de Controles Flet

## Layout
| Control | Props clave | Eventos |
|---------|-------------|---------|
| `Page` | title, theme_mode, scroll, route, views, window, overlay, pubsub, session, client_storage | on_route_change, on_keyboard_event, on_error, on_close, on_connect, on_disconnect, on_login, on_logout, on_view_pop, on_app_lifecycle_state_change, on_platform_brightness_change, on_locale_change, on_media_change |
| `View` | route, controls, appbar, navigation_bar, drawer, floating_action_button, scroll, vertical_alignment, horizontal_alignment, spacing, padding, bgcolor | — |
| `Row` | controls, alignment, spacing, wrap, scroll, expand, vertical_alignment | — |
| `Column` | controls, alignment, spacing, scroll, expand, horizontal_alignment | — |
| `Stack` | controls, expand, clip_behavior | — |
| `Container` | content, width, height, padding, margin, bgcolor, gradient, border, border_radius, shadow, alignment, blur, ink, url, animate, shape, clip_behavior, theme, theme_mode, image, blend_mode, color_filter, foreground_decoration, ignore_interactions | on_click, on_hover, on_long_press, on_tap_down, on_size_change |
| `SafeArea` | content, left, top, right, bottom, maintain_bottom_view_padding, minimum | — |
| `ResponsiveRow` | controls, columns, spacing, run_spacing | — |
| `RotatedBox` | content, rotation | — |
| `Divider` | height, thickness, color | — |
| `VerticalDivider` | width, thickness, color | — |
| `Pagelet` | content, width, height, border, border_radius, shadow | — |
| `MultiView` | views, current_index, on_view_add, on_view_remove | — |

## Texto y Tipografía
| Control | Props clave | Eventos |
|---------|-------------|---------|
| `Text` | value, size, color, bgcolor, weight, italic, font_family, selectable, max_lines, overflow, text_align, spans, style, theme_style, no_wrap, semantics_label, enable_interactive_selection | on_tap, on_selection_change |
| `TextSpan` | text, style, spans, url, semantics_label | on_click, on_enter, on_exit |
| `Markdown` | value, selectable, extension_set, code_theme, custom_code_theme, stylesheet | on_tap_link |
| `AutoComplete` | suggestions, suggestions_height | on_select |

## Botones
| Control | Props clave | Eventos |
|---------|-------------|---------|
| `Button` (ElevatedButton) | text, icon, icon_color, style, autofocus, content | on_click, on_long_press, on_hover, on_focus, on_blur |
| `FilledButton` | text, icon, style, autofocus | on_click |
| `FilledTonalButton` | text, icon, style | on_click |
| `OutlinedButton` | text, icon, style | on_click |
| `TextButton` | text, icon, style | on_click |
| `IconButton` | icon, icon_size, icon_color, style, autofocus | on_click, on_focus, on_blur |
| `FilledIconButton` | icon, icon_size, icon_color, style | on_click |
| `FilledTonalIconButton` | icon, icon_size, icon_color, style | on_click |
| `OutlinedIconButton` | icon, icon_size, icon_color, style | on_click |
| `PopupMenuButton` | items, icon, content | on_open, on_cancel |
| `MenuItemButton` | content, leading_icon, trailing_icon | on_click |
| `SubmenuButton` | content, controls | — |
| `MenuBar` | controls | — |
| `SegmentedButton` | segments, selected, show_selected_icon | on_change |
| `CupertinoButton` | content, color, border_radius, padding, opacity, disabled_color, url | on_click |
| `CupertinoFilledButton` | content, color, border_radius, padding, opacity | on_click |
| `CupertinoTintedButton` | content, color, border_radius, padding | on_click |

## Input y Formularios
| Control | Props clave | Eventos |
|---------|-------------|---------|
| `TextField` | label, hint_text, value, password, multiline, max_lines, min_lines, keyboard_type, text_align, prefix_icon, suffix_icon, prefix_text, suffix_text, helper_text, error_text, counter, border, border_color, focused_border_color, filled, bgcolor, read_only, disabled, autofocus, capitalization, input_filter, max_length | on_change, on_submit, on_focus, on_blur |
| `Dropdown` | options, value, label, hint_text, icon, autofocus, border, filled, bgcolor | on_change, on_focus, on_blur |
| `DropdownM2` | options, value, label, hint_text | on_change |
| `DropdownOption` | key, text, icon, content | — |
| `Checkbox` | label, value, tristate, autofocus, label_style, check_color, fill_color | on_change, on_focus, on_blur |
| `Switch` | label, value, autofocus, label_style, thumb_icon, active_color, inactive_color, track_color | on_change |
| `Radio` | value, label, autofocus | on_change |
| `RadioGroup` | content, value | on_change |
| `Slider` | value, min, max, divisions, label, round, autofocus, active_color, inactive_color, thumb_color, overlay_color | on_change, on_change_start, on_change_end |
| `RangeSlider` | start_value, end_value, min, max, divisions, label, autofocus | on_change, on_change_start, on_change_end |
| `DatePicker` | value, first_date, last_date, help_text, cancel_text, confirm_text, orientation, mode, entry_mode | on_change, on_dismiss, on_entry_mode_change |
| `DateRangePicker` | start_date, end_date, first_date, last_date, help_text, cancel_text, confirm_text, orientation, mode, entry_mode | on_change, on_dismiss, on_entry_mode_change |
| `TimePicker` | value, help_text, cancel_text, confirm_text, hour_format, orientation, entry_mode | on_change, on_dismiss, on_entry_mode_change |
| `ColorPicker` | color, width, height, enable_alpha, palette | on_change |
| `BlockPicker` | color, colors, columns, width, height | on_change |
| `SlidePicker` | color, width, height, enable_alpha | on_change |
| `HueringPicker` | color, width, height | on_change |
| `MaterialPicker` | color, width, height | on_change |
| `MultipleChoiceBlockPicker` | selected_colors, colors, columns, width, height | on_change |
| `SearchBar` | value, bar_hint_text, view_hint_text, controls, full_screen, divider_color, elevation | on_change, on_submit, on_focus, on_blur, on_open, on_close |
| `AutofillGroup` | content | — |

## Datos y Listas
| Control | Props clave | Eventos |
|---------|-------------|---------|
| `DataTable` | columns, rows, sort_column_index, sort_ascending, heading_row_height, data_row_height, column_spacing, heading_row_color, data_row_color, border, show_checkbox_column, checkbox_horizontal_margin | on_select_all |
| `DataColumn` | label, numeric, tooltip, on_sort | — |
| `DataRow` | cells, selected, on_select_changed, color | — |
| `DataCell` | content, placeholder, show_edit_icon, on_tap | — |
| `DataTable2` | columns, rows, sort_column_index, sort_ascending | on_select_all |
| `DataColumn2` | label, numeric, size | on_sort |
| `DataRow2` | cells, selected | on_select_changed |
| `GridView` | controls, runs_count, max_extent, spacing, run_spacing, child_aspect_ratio, padding, expand, scroll | — |
| `ListView` | controls, spacing, item_extent, padding, expand, scroll, divider_thickness | — |
| `ReorderableListView` | controls, spacing, item_extent, padding, expand, scroll | on_reorder |
| `ReorderableDragHandle` | content | — |
| `ListTile` | leading, title, subtitle, trailing, content_padding, min_leading_width, min_vertical_padding, selected, dense, enabled, shape, visual_density, title_alignment, title_text_style, subtitle_text_style, leading_and_trailing_text_style, mouse_cursor | on_click, on_long_press, on_hover, on_focus, on_blur |
| `ExpansionTile` | title, subtitle, leading, trailing, controls, initially_expanded, expanded_cross_axis_alignment, maintain_state, dense, tile_padding, shape, collapsed_shape, bgcolor, collapsed_bgcolor, icon_color, collapsed_icon_color, text_color, collapsed_text_color, clip_behavior | on_click |
| `ExpansionPanelList` | panels, expand_icon_color, elevation, divider_color | — |
| `ExpansionPanel` | header, content, bgcolor, expanded | — |
| `Chip` | label, avatar, leading_icon, trailing_icon, selected, selected_color, delete_icon, selected_color, show_checkmark, autofocus | on_click, on_delete, on_select, on_focus, on_hover |
| `Card` | content, elevation, color, shadow_color, surface_tint_color, margin, clip_behavior, border_on_foreground, semantic_container, variant | — |

## Navegación
| Control | Props clave | Eventos |
|---------|-------------|---------|
| `NavigationBar` | destinations, selected_index, label_behavior, bgcolor, elevation, shadow_color, indicator_color, indicator_shape, surface_tint_color, animation_duration, adaptive | on_change |
| `NavigationBarDestination` | icon, selected_icon, label, tooltip | — |
| `NavigationRail` | destinations, selected_index, label_type, extended, bgcolor, elevation, shadow_color, indicator_color, indicator_shape, leading, trailing, min_width, min_extended_width, group_alignment, animation_duration | on_change |
| `NavigationRailDestination` | icon, selected_icon, label, padding, indicator_color, indicator_shape | — |
| `NavigationDrawer` | controls, selected_index, bgcolor, elevation, shadow_color, surface_tint_color, indicator_color, indicator_shape, tile_padding, enable_gesture, open | on_change, on_dismiss |
| `NavigationDrawerDestination` | icon, selected_icon, label, bgcolor | — |
| `Tabs` | tabs, selected_index, scrollable, animation_duration, divider_color, indicator_color, indicator_border_radius, indicator_padding, indicator_tab_size, label_color, unselected_label_color, overlay_color, mouse_cursor, enable_feedback | on_change |
| `Tab` | text, icon, content, tab_content | — |
| `TabBar` | tabs, selected_index, indicator_color, indicator_weight, indicator_size, label_color, unselected_label_color, label_padding, mouse_cursor | on_change |
| `TabBarView` | controls, selected_index | — |
| `AppBar` | title, leading, leading_width, automatically_imply_leading, actions, bgcolor, elevation, shadow_color, surface_tint_color, toolbar_height, center_title, title_spacing, force_material_transparency, clip_behavior, scrolled_under_elevation, primary | — |
| `BottomAppBar` | content, bgcolor, elevation, shadow_color, surface_tint_color, shape, clip_behavior, notch_margin, padding | — |
| `CupertinoAppBar` | title, leading, trailing, bgcolor, automatically_imply_leading, large_title, transition_between_routes, previous_page_title | — |
| `CupertinoNavigationBar` | destinations, selected_index, bgcolor, active_color, inactive_color, border | on_change |
| `Router` | routes, not_found_route | — |

## Diálogos y Notificaciones
| Control | Props clave | Eventos |
|---------|-------------|---------|
| `AlertDialog` | title, content, actions, actions_alignment, modal, bgcolor, elevation, shadow_color, surface_tint_color, icon, shape, clip_behavior, inset_padding, actions_padding, button_padding, content_padding, title_padding, semantic_label | on_dismiss |
| `Banner` | content, leading, actions, bgcolor, elevation, shadow_color, surface_tint_color, padding, leading_padding, force_actions_below, content_text_style | on_visible |
| `BottomSheet` | content, bgcolor, elevation, shadow_color, surface_tint_color, shape, clip_behavior, enable_drag, show_drag_handle, drag_handle_color, use_safe_area, is_scroll_controlled, maintain_bottom_view_insets_padding, enable_gesture | on_dismiss |
| `SnackBar` | content, bgcolor, elevation, shadow_color, surface_tint_color, shape, clip_behavior, action, action_color, action_overflow_threshold, behavior, duration, dismiss_direction, show_close_icon, close_icon_color, padding, width, margin | — |
| `CupertinoAlertDialog` | title, content, actions, bgcolor | — |
| `CupertinoActionSheet` | title, message, actions, cancel, bgcolor | — |
| `CupertinoActionSheetAction` | text, is_default_action, is_destructive_action | on_click |
| `CupertinoDialogAction` | text, is_default_action, is_destructive_action | on_click |

## Multimedia e Imágenes
| Control | Props clave | Eventos |
|---------|-------------|---------|
| `Image` | src, width, height, fit, border_radius, repeat, color, color_blend_mode, gapless_playback, match_text_direction, filter_quality, error_builder | on_loaded, on_error |
| `RawImage` | width, height, pixel_format, bytes, fit | — |
| `Icon` | name, size, color, semantic_label | — |
| `CircleAvatar` | content, foreground_image_url, background_image_url, radius, min_radius, max_radius, bgcolor, on_background_image_error | — |
| `Video` | playlist, configuration, aspect_ratio, volume, playback_rate, show_controls, filter_quality, fill, wakelock, autoplay, subtitle_configuration | on_loaded, on_enter_pip, on_leave_pip, on_completed, on_error, on_resume, on_pause, on_seek, on_position_change, on_duration_change, on_state_change |
| `Audio` | src, autoplay, volume, balance, playback_rate, release_mode | on_loaded, on_duration_change, on_position_change, on_state_change, on_seek_complete |
| `Camera` | value, lens_direction, resolution_preset, enable_audio, image_format, exposure_mode, flash_mode, focus_mode | on_image, on_state_change |
| `Lottie` | src, width, height, repeat, reverse, autoplay, animate, background_loading, renderer, filter_quality | on_loaded, on_error |
| `Rive` | src, width, height, artboard, animation, autoplay, antialiasing, fit, alignment | on_loaded, on_error |
| `Canvas` | shapes, width, height, resize_interval | on_resize |
| `MatplotlibChart` | figure, isolated, transparent, original_size | — |
| `PlotlyChart` | figure, isolated | — |
| `Shimmer` | content, width, height, bgcolor, highlight_color, period, direction | — |

## Gráficos (Charts)
| Control | Props clave | Eventos |
|---------|-------------|---------|
| `BarChart` | bar_groups, groups_space, bar_width, tooltip_bgcolor, tooltip_direction, interactive, animate | on_chart_event |
| `LineChart` | data_series, tooltip_bgcolor, interactive, animate, min_x, max_x, min_y, max_y | on_chart_event |
| `PieChart` | sections, sections_space, center_space, start_degree, tooltip_bgcolor, interactive, animate | on_chart_event |
| `RadarChart` | data_sets, title, border_color, border_width, grid_line_color, grid_line_width, tick_count, tick_label_style, range_angle, range_radius, interactive | on_chart_event |
| `ScatterChart` | spots, tooltip_bgcolor, interactive, animate | on_chart_event |
| `CandlestickChart` | spots, tooltip_bgcolor, interactive, animate | on_chart_event |

## Avanzados
| Control | Props clave | Eventos |
|---------|-------------|---------|
| `WebView` | url, content, width, height, javascript_enabled, allow_dialogs, allow_downloads, enable_zoom, enable_local_storage, enable_video, enable_audio, enable_sensors, enable_smart_zoom, enable_drag_to_resize, enable_drop_to_upload, enable_media_controls, enable_web_inspector, user_agent, background_color, configuration | on_page_started, on_page_ended, on_progress, on_url_change, on_console_message, on_javascript_event, on_scroll |
| `Map` | initial_camera, layers, interactive, configuration | on_event, on_hover, on_pointer, on_position_change, on_tap |
| `CodeEditor` | value, language, theme, custom_theme, read_only, show_line_numbers, show_folding_handles, highlight_active_line, line_numbers, gutter_style, font_family, font_size, min_height, max_height, tab_size, word_wrap, autofocus | on_change, on_focus, on_blur |
| `InteractiveViewer` | content, min_scale, max_scale, boundary_margin, interaction_end_friction, constrained, pan_enabled, scale_enabled | on_interaction_start, on_interaction_end, on_interaction_update |
| `GestureDetector` | content, mouse_cursor, drag_interval | on_tap, on_double_tap, on_long_press, on_secondary_tap, on_secondary_long_press, on_triple_tap, on_enter, on_exit, on_hover, on_pan_start, on_pan_update, on_pan_end, on_scale_start, on_scale_update, on_scale_end, on_vertical_drag_start, on_vertical_drag_update, on_vertical_drag_end, on_horizontal_drag_start, on_horizontal_drag_update, on_horizontal_drag_end |
| `KeyboardListener` | content | on_key_event |
| `Draggable` | content, feedback, child_when_dragging, data, max_simultaneous_drags, delay, affinity, mouse_cursor | on_drag_start, on_drag_end, on_drag_complete |
| `DragTarget` | content, group, data | on_will_accept, on_accept, on_leave, on_move |
| `Dismissible` | content, background, secondary_background, confirm_dismiss, direction, resize_duration, dismiss_thresholds, movement_duration, cross_axis_end_offset | on_dismiss, on_update, on_resize, on_confirm_dismiss |
| `ContextMenu` | controls, bgcolor, elevation, shape, trigger | on_dismiss, on_select |
| `MenuBar` | controls | — |
| `Hero` | tag, content, flight_shuttle, placeholder_filler, create_rect_tween, transition_on_user_gestures | — |
| `Placeholder` | width, height, color, stroke_width, lines, label, label_alignment, fallback_width, fallback_height | — |
| `ProgressBar` | value, bar_height, color, bgcolor, border_radius, semantics_label, semantics_value | — |
| `ProgressRing` | value, stroke_width, color, bgcolor, semantics_label, semantics_value | — |
| `SpinKit` | type, size, color | — |
| `FloatingActionButton` | content, icon, text, bgcolor, foreground_color, elevation, shape, mini, autofocus, mouse_cursor, enable_feedback, tooltip, hero_tag, clip_behavior, focus_color, focus_elevation, highlight_elevation, hover_elevation, disabled_elevation, splash_color | on_click |
| `AnimatedSwitcher` | content, transition, duration, reverse_duration, switch_in_curve, switch_out_curve | — |
| `Screenshot` | content, width, height | — |
| `ShaderMask` | content, shader_callback, blend_mode | — |
| `SelectionArea` | content | — |
| `Semantics` | content, label, value, increased_value, decreased_value, hint, on_tap_hint, on_long_press_hint, on_scroll_left_hint, on_scroll_right_hint, on_scroll_up_hint, on_scroll_down_hint, exclude_semantics, button, header, link, image, text_field, slider, checkbox, switch, radio, multiline, selected, focusable, focused, toggled, expanded, hidden, readonly, live_region, container, muted | — |
| `MergeSemantics` | content | — |
| `TransparentPointer` | content | — |
| `WindowDragArea` | content | — |
| `SafeArea` | content, left, top, right, bottom, maintain_bottom_view_padding, minimum | — |
| `Badge` | content, label, label_style, offset, small_size, large_size, alignment, bgcolor, text_color, padding | — |
| `Tooltip` | message, content, wait_duration, exit_duration, prefer_below, vertical_offset, horizontal_offset, decoration, text_style, enable_feedback, trigger_mode, margin, padding, height, width | — |

## iOS (Cupertino)
| Control | Props clave |
|---------|-------------|
| `CupertinoActivityIndicator` | radius, animating, progress |
| `CupertinoCheckbox` | value, tristate, active_color, inactive_color, check_color, shape |
| `CupertinoRadio` | value, active_color, inactive_color, toggleable |
| `CupertinoSwitch` | value, active_color, track_color, thumb_color, on_label, off_label |
| `CupertinoSlider` | value, min, max, divisions, active_color, inactive_color, thumb_color, on_change_start, on_change_end |
| `CupertinoSegmentedButton` | controls, selected_index, bgcolor, border_color, unselected_color, selected_color, pressed_color |
| `CupertinoSlidingSegmentedButton` | controls, selected_index, bgcolor, thumb_color, unselected_color, selected_color |
| `CupertinoTextField` | value, placeholder, prefix, suffix, clear_button, padding, keyboard_type, autofocus, max_length, max_lines, min_lines, multiline, password, read_only, capitalization, text_align, text_style, bgcolor, border, border_radius, cursor_color, cursor_width, cursor_height, enable_interactive_selection, selection_color, smart_dashes_type, smart_quotes_type |
| `CupertinoDatePicker` | value, date_order, mode, min_year, max_year, minute_interval, bgcolor |
| `CupertinoTimerPicker` | value, mode, bgcolor, minute_interval, second_interval |
| `CupertinoPicker` | selected_index, controls, bgcolor, magnification, item_extent, diameter_ratio, looping, off_axis_fraction, squeeze, use_text_selection |
| `CupertinoListTile` | title, subtitle, leading, trailing, bgcolor, padding, additional_info |
| `CupertinoBottomSheet` | content, bgcolor, height, corner_radius, enable_backdrop, blur_radius, support_stretching, use_safe_area |
| `CupertinoContextMenu` | content, controls, bgcolor, enable_haptic_feedback |
| `CupertinoContextMenuAction` | text, is_default_action, is_destructive_action, trailing_icon |

## Canvas Shapes
| Shape | Props clave |
|-------|-------------|
| `CanvasArc` | x, y, width, height, start_angle, sweep_angle, paint, use_center |
| `CanvasCircle` | x, y, radius, paint |
| `CanvasColor` | color, alpha |
| `CanvasFill` | paint |
| `CanvasImage` | src, x, y, width, height, fit, filter_quality |
| `CanvasLine` | x1, y1, x2, y2, paint |
| `CanvasOval` | x, y, width, height, paint |
| `CanvasPath` | moves, paint |
| `CanvasPoints` | points, point_mode, paint |
| `CanvasRect` | x, y, width, height, paint, border_radius |
| `CanvasShadow` | shadow, content |
| `CanvasShape` | content, paint |
| `CanvasText` | text, x, y, style, alignment, max_lines, max_width, text_align |

## Map Layers
| Layer | Props clave |
|-------|-------------|
| `TileLayer` | url_template, subdomains, max_zoom, min_zoom, tile_size, tms, opacity, keep_alive, enable_retina_mode, user_agent_package_name, zoom_min, zoom_max, wms_configuration, tile_display, evict_error_tile_strategy, max_zoom_gesture_retention, additional_options, backgroundColor, userAgent, userAgentPackageName, errorImage, tileBuilder, minTileLevel, maxTileLevel, tileUpdateProvider, keepAlive, enableRetinaMode, enableCaching |
| `MarkerLayer` | markers, alignment, rotate, rotate_origin, width, height, anchor |
| `CircleLayer` | circles |
| `PolygonLayer` | polygons |
| `PolylineLayer` | polylines |
| `OverlayImageLayer` | overlay_images |
| `Marker` | point, width, height, alignment, rotate, rotate_origin, child |
| `CircleMarker` | point, radius, color, border_color, border_stroke_width, use_radius_in_meters, coordinates |
| `PolygonMarker` | points, color, border_color, border_stroke_width, filled, label, label_text_style, label_alignment, label_padding, use_center_for_label, is_dotted, dotted_stroke_pattern, dashed_stroke_pattern, stroke_pattern, disable_holes_border |
| `PolylineMarker` | points, color, border_color, border_stroke_width, is_dotted, dotted_stroke_pattern, dashed_stroke_pattern, stroke_pattern, use_stroke_width_in_meter, gradient |
| `OverlayImage` | image, bounds, height, width, start_x, start_y, end_x, end_y, visible, opacity |
| `RotatedOverlayImage` | image, bounds, height, width, start_x, start_y, end_x, end_y, visible, opacity, rotation |
| `BaseOverlayImage` | image, bounds, height, width, start_x, start_y, end_x, end_y, visible, opacity |
| `ImageSourceAttribution` | source, text, image, on_click, width, height, anchor, alignment, offset |
| `SimpleAttribution` | text, on_click, width, height, anchor, alignment, offset |
| `TextSourceAttribution` | text, on_click, width, height, anchor, alignment, offset |
| `RichAttribution` | attributions, popup_initial_scale, popup_initial_rotation, popup_button_rotation, popup_button_anchor, popup_button_offset, popup_button_anchor_radii, popup_snap_animation, popup_brand_logo, popup_brand_logo_anchor, popup_brand_logo_offset, popup_brand_logo_anchor_radii, popup_brand_logo_fit, primary_attribution, secondary_attribution, secondary_attribution_anchor, secondary_attribution_offset, secondary_attribution_anchor_radii, secondary_attribution_always_visible |

## Ads
| Control | Props clave | Eventos |
|---------|-------------|---------|
| `BannerAd` | unit_id, sizes, ad_request, listener | on_loaded, on_failed_to_load, on_opened, on_closed, on_clicked, on_impression, on_will_dismiss, on_dismissed, on_will_present, on_presented, on_scored, on_paid_event |
| `InterstitialAd` | unit_id, ad_request, listener | on_loaded, on_failed_to_load, on_opened, on_closed, on_clicked, on_impression, on_will_dismiss, on_dismissed, on_will_present, on_presented, on_scored, on_paid_event |
| `ConsentManager` | consent_request_parameters, debug_settings, listener | on_consent_info_update, on_consent_form_load_failure, on_consent_form_dismissed |