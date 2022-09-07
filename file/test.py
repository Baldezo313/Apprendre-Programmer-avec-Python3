# varjob = "Patch Set 11: Verified+1\n\n" \
#          "Check succeeded.\n\n\n\n" \
#          "Success:\n\n" \
#          "- https://ece-ci.dynamic.nsn-net.net/job/CI_TOOLS/job/CHECKOUT/job/FAST_CHECKOUT/469538/ : SUCCESS in 56s\n" \
#          "- https://ece-ci.dynamic.nsn-net.net/job/MASTER/job/GNB/job/COMMON/job/STATIC_CHECK/40381/ : SUCCESS in 2m 11s\n" \
#          "- https://ece-ci.dynamic.nsn-net.net/job/MASTER/job/GNB/job/CPLANE/job/CP-RT/job/BUILD.simple.cmpr/1047/ : SUCCESS in 3m 13s\n" \
#          "- https://ece-ci.dynamic.nsn-net.net/job/MASTER/job/GNB/job/CPLANE/job/CP-RT/job/BUILD.simple.sm6-snowfish/42445/ : SUCCESS in 2m 53s\n" \
#          "- https://ece-ci.dynamic.nsn-net.net/job/MASTER/job/GNB/job/CPLANE/job/CP-RT/job/CMAKE_SANITY_CHECK.simple.native/21521/ : SUCCESS in 53s\n" \
#          "- https://ece-ci.dynamic.nsn-net.net/job/MASTER/job/GNB/job/CPLANE/job/CP-RT/job/COVERAGE.ut.native/70447/ : SUCCESS in 5m 29s\n" \
#          "- https://ece-ci.dynamic.nsn-net.net/job/MASTER/job/GNB/job/CPLANE/job/CP-RT/job/CPD.cxx/74624/ : SUCCESS in 50s\n" \
#          "- https://ece-ci.dynamic.nsn-net.net/job/MASTER/job/GNB/job/CPLANE/job/CP-RT/job/FORMAT.prodcode.native/76439/ : SUCCESS in 1m 22s\n" \
#          "- https://ece-ci.dynamic.nsn-net.net/job/MASTER/job/GNB/job/CPLANE/job/CP-RT/job/LINT.sct_ttcn3.native/93909/ : SUCCESS in 2m 20s\n" \
#          "- https://ece-ci.dynamic.nsn-net.net/job/MASTER/job/GNB/job/CPLANE/job/CP-RT/job/NOLINT.cxx/74324/ : SUCCESS in 47s\n" \
#          "- https://ece-ci.dynamic.nsn-net.net/job/MASTER/job/GNB/job/CPLANE/job/CP-RT/job/SCT_TTCN3.simple.native/95621/ : SUCCESS in 13m 22s\n" \
#          "- https://ece-ci.dynamic.nsn-net.net/job/MASTER/job/GNB/job/CPLANE/job/CP-RT/job/SCT_TTCN3.ubsanitizer_clang.native/78802/ : SUCCESS in 10m 05s\n" \
#          "- https://ece-ci.dynamic.nsn-net.net/job/MASTER/job/GNB/job/CPLANE/job/CP-RT/job/TIDY.cxx_prodcode.native/75097/ : SUCCESS in 3m 21s\n" \
#          "- https://ece-ci.dynamic.nsn-net.net/job/MASTER/job/GNB/job/CPLANE/job/CP-RT/job/UT.aubsanitizer.native/64190/ : SUCCESS in 5m 53s\n" \
#          "- https://ece-ci.dynamic.nsn-net.net/job/MASTER/job/GNB/job/CPLANE/job/CP-RT/job/UT.aubsanitizer_clang.native/19188/ : SUCCESS in 5m 42s\n" \
#          "- https://ece-ci.dynamic.nsn-net.net/job/MASTER/job/GNB/job/CPLANE/job/CP-RT/job/UT.tsanitizer.native/76645/ : SUCCESS in 3m 07s\n" \
#          "- https://ece-ci.dynamic.nsn-net.net/job/MASTER/job/GNB/job/CPLANE/job/CP-RT/job/UT.valgrind.native/75950/ : SUCCESS in 14m 51s\n" \
#          "- https://ece-ci.dynamic.nsn-net.net/job/MASTER/job/GNB/job/CPLANE/job/CU/job/COMMON/job/CPD.ttcn3.native/116637/ : SUCCESS in 1m 21s\n\n" \
#          "Non-voting:\n\n" \
#          "- https://ece-ci.dynamic.nsn-net.net/job/MASTER/job/GNB/job/CPLANE/job/CP-RT/job/COVERAGE.ut_html.native/52757/ : SUCCESS in 6m 05s (non-voting)\n\n" \
#          "Please notice that it's under Without Zuul Rebase Policy."

# varParentId = "Patch Set 11:\n\nRebase age choice - branch_head:\n" \
#               "[zuul-base]a2b18ed672cdf60c1e27867eedb803e63d5b4b45[zuul-base]\n" \
#               "[zuul-date-utc] 2022-08-03 09:12:00.081000000 [zuul-date-utc].\n" \
#               "[zuul-url] http://eslinb34.emea.nsn-net.net:8881/p [zuul-url]"
# ####################################################################################################

pairs = {"1": 'a', "2": 'b', "3": 'c', "4": 'd'}
for _, val in pairs.items():
    status = list(zip(*val))
    print(status)

