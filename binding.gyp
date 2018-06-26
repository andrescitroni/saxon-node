{
    'targets': [
        {
            'target_name': 'saxonXslt',
            'conditions': [
            ['OS=="linux"', {
                'cflags!': [ '-fno-exceptions' ],
                'cflags_cc!': [ '-fno-exceptions' ],
                'cflags': ["-fPIC", "-O4", "-DCPP_ONLY", "-std=c++11", "-fexceptions", "-Wl,--allow-multiple-definition"],
                'include_dirs': [
                    '$(SAXONC_HOME)/Saxon.C.API',
                    '$(JAVA_HOME)/include',
                    '$(JAVA_HOME)/include/linux',
                    'src/'
                ],
                'sources': [
                    'src/SaxonCGlue.c',
                    'src/SaxonCXPath.c',
                    'src/SaxonProcessor.cpp',
                    'src/XsltProcessor.cpp',
                    'src/XQueryProcessor.cpp',
                    'src/XPathProcessor.cpp',
                    'src/SchemaValidator.cpp',
                    'src/XdmItem.cpp',
                    'src/XdmValue.cpp',
                    'src/XdmNode.cpp',
                    'src/XdmAtomicValue.cpp',
                    'src/XdmValueJS.cxx',
                    'src/XdmItemJS.cxx',
                    'src/XdmNodeJS.cxx',
                    'src/XdmAtomicValueJS.cxx',
                    'src/SaxonProcessorJS.cxx',
                    'src/saxonXslt.cxx'
                ],
                'link_settings': {
                    'libraries': [
                    ],
                    'ldflags': [
                        '-L$(SAXONC_HOME)'
                    ]
                }
            }],
            ['OS=="win"', {
                'include_dirs': [
                    "<!(echo %SAXONC_HOME%)/Saxon-C-API",
                    "<!(echo %JAVA_HOME%)/include",
                    "<!(echo %JAVA_HOME%)/include/win32",
                    "./src",
                    "C:\\Software\\node-v0.12.7\\src",
                    "C:\\Software\\node-v0.12.7\\deps\\v8\\include"
                ],
                'sources': [
                    'src/SaxonProcessor.cpp',
                    'src/SaxonProcessorJS.cxx',
                    'src/saxonXslt.cxx'
                ],
                'msbuild_toolset': 'v120',
                "configurations": {
                            "Release": {
                'msvs_settings':
                {
                    'VCCLCompilerTool':
                    {
                        'RuntimeLibrary': 2,        # shared release
                        'ExceptionHandling': 1,     # /EHsc
                        "PreprocessorDefinitions" :
                        [
                            "CPP_ONLY"
                        ],
                        'AdditionalOptions': 
                        [
                            '/EHsc' # Enable unwind semantics for Exception Handling.  This one actually does the trick - and no warning either.
                        ]
                    }
                }
              }
              },
                'link_settings': {
                    'libraries': [
                    ]
                }
            }],
            ['OS=="mac"', {
                'xcode_settings': {
                    'OTHER_CPLUSPLUSFLAGS': ["-fPIC", "-O3", "-DCPP_ONLY", "-std=c++11", "-fexceptions","-v"],
                    'OTHER_LDFLAGS': []
                },
                'include_dirs': [
                    '$(SAXONC_HOME)/Saxon.C.API',
                    '$(JAVA_HOME)/include',
                    '$(JAVA_HOME)/include/darwin',
                    'src/'
                ],
                'sources': [
                    'src/SaxonCGlue.c',
                    'src/SaxonCXPath.c',
                    'src/SaxonProcessor.cpp',
                    'src/XsltProcessor.cpp',
                    'src/XQueryProcessor.cpp',
                    'src/XPathProcessor.cpp',
                    'src/SchemaValidator.cpp',
                    'src/XdmItem.cpp',
                    'src/XdmValue.cpp',
                    'src/XdmNode.cpp',
                    'src/XdmAtomicValue.cpp',
                    'src/XdmValueJS.cxx',
                    'src/XdmItemJS.cxx',
                    'src/XdmNodeJS.cxx',
                    'src/XdmAtomicValueJS.cxx',
                    'src/SaxonProcessorJS.cxx',
                    'src/saxonXslt.cxx'
                ],
                'link_settings': {
                    'libraries': [
                    ],
                    'ldflags': [
                        '-L$(SAXONC_HOME)'
                    ]
                }
            }]
           ]
        },
        {
            "target_name": "action_after_build",
            "type": "none",
            "dependencies": [ "saxonXslt" ],
            "copies": [
            {
              "files": [ "<(PRODUCT_DIR)/saxonXslt.node" ],
              "destination": "./lib/binding/"
            }
            ]
        }        
    ]
}
