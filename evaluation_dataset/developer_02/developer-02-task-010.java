private void configureWindow(WebWindow web) {
        if (m_fullscreen) {
            m_width = web.width();
            m_height = web.height();
            web.showFullScreen();
        } else {
            web.showNormal();
            if (! m_resizable) {
               web.setFixedSize(new QSize(m_width, m_height));
            } else {
               web.setBaseSize(new QSize(m_width, m_height));
            }
            web.resize(m_width, m_height);
        }
        if (! m_bar) {
            web.menuBar().setVisible(false);
        } else {
            web.menuBar().setVisible(true);
            if (m_icon != null) {
                QIcon icon = new QIcon(m_icon);
                web.setWindowIcon(icon);
            }
            web.setWindowTitle(m_appName);
        }
        if (! m_contextMenu) {
            web.setContextMenuPolicy(ContextMenuPolicy.PreventContextMenu);
        } else {
            web.setContextMenuPolicy(ContextMenuPolicy.DefaultContextMenu);
        }
    }