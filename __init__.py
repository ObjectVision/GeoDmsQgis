# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Geodms
                                 A QGIS plugin
 Geodms plugin for qgis
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2025-03-28
        copyright            : (C) 2025 by Object Vision BV
        email                : eoudejans@objectvision.nl
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Geodms class from file Geodms.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .geodms_qgis import GeodmsQgis
    return GeodmsQgis(iface)
