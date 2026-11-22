package com.beril.lab;

import android.app.Activity;
import android.os.Bundle;
import android.widget.TextView;

public class DebugActivity extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        TextView tv = new TextView(this);
        String extra = getIntent().getStringExtra("dump");
        tv.setText("debug dump: " + extra + "\napi: http://app.lab.local/api/\n");
        setContentView(tv);
    }
}
