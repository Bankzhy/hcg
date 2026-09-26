public void actionPerformed(ActionEvent event)
    {
        String action = event.getActionCommand();
        if ("OK".equals(action))
        {
            if (state.getState().equals(WorkPanelState.NOT_SAVED))
            {
                saveWork();
            }
        }
        else if ("Cancel".equals(action))
        {
            if (state.getState().equals(WorkPanelState.NOT_SAVED))
            {
                discardWork();
            }
        }
        else if ("Apply".equals(action))
        {
            if (state.getState().equals(WorkPanelState.NOT_SAVED))
            {
                saveWork();
            }
        }
    }