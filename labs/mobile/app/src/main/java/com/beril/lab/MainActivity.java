package com.beril.lab;

import android.app.Activity;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.webkit.JavascriptInterface;
import android.webkit.WebView;

public class MainActivity extends Activity {
    private WebView web;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        web = new WebView(this);
        web.getSettings().setJavaScriptEnabled(true);
        web.addJavascriptInterface(new Bridge(), "BerilBridge");
        setContentView(web);

        Uri data = getIntent().getData();
        if (data != null) {
            String target = data.getQueryParameter("url");
            if (target != null) {
                web.loadUrl(target);
            }
        } else {
            web.loadUrl("https://app.lab.local/index.html");
        }
    }

    class Bridge {
        @JavascriptInterface
        public String token() {
            return "tok_lab_7f3a9c";
        }

        @JavascriptInterface
        public void open(String url) {
            startActivity(new Intent(Intent.ACTION_VIEW, Uri.parse(url)));
        }
    }
}
